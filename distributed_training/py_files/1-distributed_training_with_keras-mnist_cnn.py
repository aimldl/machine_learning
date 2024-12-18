#!/usr/bin/env python
# coding: utf-8

# ##### Copyright 2019 The TensorFlow Authors.
#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Source:
#   [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)
#   The source code is edited by T Kim.
#
## Overview
# 
# The `tf.distribute.Strategy` API provides an abstraction for distributing your training
# across multiple processing units. The goal is to allow users to enable distributed training using existing models and training code, with minimal changes.
# 
# This tutorial uses the `tf.distribute.MirroredStrategy`, which
# does in-graph replication with synchronous training on many GPUs on one machine.
# Essentially, it copies all of the model's variables to each processor.
# Then, it uses [all-reduce](http://mpitutorial.com/tutorials/mpi-reduce-and-allreduce/) to combine the gradients from all processors and applies the combined value to all copies of the model.
# 
# `MirroredStrategy` is one of several distribution strategy available in TensorFlow core. You can read about more strategies at [distribution strategy guide](../../guide/distributed_training.ipynb). 

# ### Keras API
# This example uses the `tf.keras` API to build the model and training loop. For custom training loops, see the [tf.distribute.Strategy with training loops](training_loops.ipynb) tutorial.

# Import TensorFlow and TensorFlow Datasets
import tensorflow_datasets as tfds
import tensorflow as tf
import os

print(tf.__version__)

# ## Download the dataset
# Download the MNIST dataset and load it from [TensorFlow Datasets](https://www.tensorflow.org/datasets). This returns a dataset in `tf.data` format.
# Setting `with_info` to `True` includes the metadata for the entire dataset, which is being saved here to `info`.
# Among other things, this metadata object includes the number of train and test examples. 
datasets, info = tfds.load(name='mnist', with_info=True, as_supervised=True)
mnist_train, mnist_test = datasets['train'], datasets['test']

# ## Define distribution strategy
# Create a `MirroredStrategy` object. This will handle distribution, and provides a context manager (`tf.distribute.MirroredStrategy.scope`) to build your model inside.
strategy = tf.distribute.MirroredStrategy()
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))

# ## Setup input pipeline
# When training a model with multiple GPUs, you can use the extra computing power effectively by increasing the batch size. In general, use the largest batch size that fits the GPU memory, and tune the learning rate accordingly.
# You can also do info.splits.total_num_examples to get the total
# number of examples in the dataset.
num_train_examples = info.splits['train'].num_examples
num_test_examples = info.splits['test'].num_examples
BUFFER_SIZE = 10000
BATCH_SIZE_PER_REPLICA = 64
BATCH_SIZE = BATCH_SIZE_PER_REPLICA * strategy.num_replicas_in_sync

# Pixel values, which are 0-255, [have to be normalized to the 0-1 range](https://en.wikipedia.org/wiki/Feature_scaling). Define this scale in a function.
def scale(image, label):
  image = tf.cast(image, tf.float32)
  image /= 255
  return image, label

# Apply this function to the training and test data, shuffle the training data, and [batch it for training](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch). Notice we are also keeping an in-memory cache of the training data to improve performance.
train_dataset = mnist_train.map(scale).cache().shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
eval_dataset = mnist_test.map(scale).batch(BATCH_SIZE)

# ## Create the model
# Create and compile the Keras model in the context of `strategy.scope`.
with strategy.scope():
  model = tf.keras.Sequential([
      tf.keras.layers.Conv2D(32, 3, activation='relu', input_shape=(28, 28, 1)),
      tf.keras.layers.MaxPooling2D(),
      tf.keras.layers.Flatten(),
      tf.keras.layers.Dense(64, activation='relu'),
      tf.keras.layers.Dense(10)
  ])

  model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                optimizer=tf.keras.optimizers.Adam(),
                metrics=['accuracy'])

# ## Define the callbacks
# The callbacks used here are:
# 
# * TensorBoard             This callback writes a log for TensorBoard which allows you to visualize the graphs.
# * Model Checkpoint        This callback saves the model after every epoch.
# * Learning Rate Scheduler Using this callback, you can schedule the learning rate to change after every epoch/batch.
# 
# For illustrative purposes, add a print callback to display the learning rate in the notebook.

# Define the checkpoint directory to store the checkpoints
checkpoint_dir = './training_checkpoints'
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

# Function for decaying the learning rate.
# You can define any decay function you need.
def decay(epoch):
  if epoch < 3:
    return 1e-3
  elif epoch >= 3 and epoch < 7:
    return 1e-4
  else:
    return 1e-5

# Callback for printing the LR at the end of each epoch.
class PrintLR(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs=None):
    print('\nLearning rate for epoch {} is {}'.format(epoch + 1,
                                                      model.optimizer.lr.numpy()))

callbacks = [
    tf.keras.callbacks.TensorBoard(log_dir='./logs'),
    tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_prefix,
                                       save_weights_only=True),
    tf.keras.callbacks.LearningRateScheduler(decay),
    PrintLR()
]

# ## Train and evaluate
# Now, train the model in the usual way, calling `fit` on the model and passing in the dataset created at the beginning of the tutorial. This step is the same whether you are distributing the training or not.
model.fit(train_dataset, epochs=12, callbacks=callbacks)

# As you can see below, the checkpoints are getting saved.
# check the checkpoint directory
#get_ipython().system('ls {checkpoint_dir}')
command = f'ls {checkpoint_dir}'
print(command)
os.system(command)

# To see how the model perform, load the latest checkpoint and call `evaluate` on the test data.
# Call `evaluate` as before using appropriate datasets.
model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
eval_loss, eval_acc = model.evaluate(eval_dataset)
print('Eval loss: {}, Eval Accuracy: {}'.format(eval_loss, eval_acc))

# To see the output, you can download and view the TensorBoard logs at the terminal.
# ```
# $ tensorboard --logdir=path/to/log-directory
# ```
#get_ipython().system('ls -sh ./logs')
command = 'ls -sh ./logs'
print(command)
os.system(command)

# ## Export to SavedModel
# Export the graph and the variables to the platform-agnostic SavedModel format. After your model is saved, you can load it with or without the scope.
path = 'saved_model/'
model.save(path, save_format='tf')

# Load the model without `strategy.scope`.
unreplicated_model = tf.keras.models.load_model(path)
unreplicated_model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(),
    metrics=['accuracy'])
eval_loss, eval_acc = unreplicated_model.evaluate(eval_dataset)
print('Eval loss: {}, Eval Accuracy: {}'.format(eval_loss, eval_acc))

# Load the model with `strategy.scope`.
with strategy.scope():
  replicated_model = tf.keras.models.load_model(path)
  replicated_model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                           optimizer=tf.keras.optimizers.Adam(),
                           metrics=['accuracy'])
  eval_loss, eval_acc = replicated_model.evaluate(eval_dataset)
  print ('Eval loss: {}, Eval Accuracy: {}'.format(eval_loss, eval_acc))
