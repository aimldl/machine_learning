##### aimldl > bindsnet > configure.md

# 1. Configure the Computing Environment
Among several options for the computing environment, a Conda virtual environment is set up for [BindsNET](https://github.com/BindsNET).

### 1.1. Set up the Virtual Environment for BindsNET
```bash
(base) ~$ conda update -n base -c defaults conda
(base) ~$ conda create -n bindsnet
```
Anaconda is updated to the latest version and a virtual environment named "bindsnet" is created.
For details, refer to [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) and [conda create](https://docs.conda.io/projects/conda/en/latest/commands/create.html).

### 1.1.1. Activate or Deactivate the Virtual Environment
To enter or activate the virtual environment, run:
```bash
(base) ~$ conda activate bindsnet
(bindsnet) ~$
```
Notice "(base)" is changed to "(bindsnet)".

To exit or deactivate the virtual environment, run:
```bash
(bindsnet) ~$ conda deactivate
(base) $
```
Notice the virtual environment "bindsnet" is changed to the "base" environment.

### 1.1.2. Check the Existing Virtual Environments
To see the created virtual environments, check the information about the environments with one of the commands. Note -e is the short-hand notation for --envs.
```bash
$ conda info --envs
$ conda info -e
$ conda env list
```
They present the same output like below.
```bash
(base) aimldl@GPU-Desktop:~$ conda info --envs
# conda environments:
#
base                  *  /home/aimldl/anaconda3
bindsnet                 /home/aimldl/anaconda3/envs/bindsnet
  ...
(base) ~$
```
I see "bindsnet" below the "base" environment along with other environments which are listed as "...".

### 1.1.3. Directory for BindNET
A new directory is created for a new virtual envinronment. So directory "bindsnet" is created below directory "~/anaconda3/envs". (If you didn't choose the default directory, see "your_base_directory/envs".)
You may check if the directory for "bindsnet" exists under the default envs directory.
```bash
(base) ~$ ls ~/anaconda3/envs/
bindsnet ...
(base) ~$
```

### 1.2. Install the Required Packages
Installing the required packages with "$ pip install -r requirements.txt" failed. The following commands fixed the problem and installed the required packages properly. Refer to [troubleshooting.md](#troubleshooting.md) if you're interested in how the errors are fixed during the installation process.

```bash
$ conda install -c pytorch pytorch
$ pip install foolbox scipy numpy torch  torchvision tqdm setuptools matplotlib gym scikit_image scikit_learn opencv-python sphinx_rtd_theme pytest cython pandas tensorboardX pre-commit
$ pip install pip install bindsnet
```
### 1.3. Verify the installation
When the installation is done, test if BindsNET runs properly.
```bash
$ cd examples/mnist
$ python eth_mnist.py
```

In my case, the command downloaded several datasets and begain training.
```bash
(bindsnet) ~/aimldl/bindsnet/original/examples/mnist$ python eth_mnist.py
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw/train-images-idx3-ubyte.gz
  ...
  Processing...
  Done!

  Begin training.

  Progress: 0 / 1 (0.0000 seconds)
  9920512it [00:30, 570776.55it/s]
  All activity accuracy: 9.20 (last), 9.20 (average), 9.20 (best)
  Proportion weighting accuracy: 9.20 (last), 9.20 (average), 9.20 (best) 250/60000 [00:50<3:18:58,  5.00it/s]
    ...
```
(EOF)
