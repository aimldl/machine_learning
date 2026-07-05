##### aimldl > bindsnet > troubleshooting.md

# 1. Troubleshooting
This page is about how I fixed the broken chains to set up the computing environments for BindsNET. I hope this helps someone else.

### 1.1. Problem
The required packages [requirements.txt](#https://github.com/BindsNET/bindsnet/blob/master/requirements.txt) didn't install as it described in [BindsNET](#https://github.com/BindsNET/bindsnet)'s [README.md](#https://github.com/BindsNET/bindsnet/blob/master/README.md).

### 1.2. Step-by-Step
#### 1.2.1. Git clone bindsnet
I created a new directory "aimldl/bindsnet" and git-cloned BindsNET. A new directory name "original" is assigned.
```bash
(bindsnet) ~/aimldl/bindsnet$ git clone https://github.com/BindsNET/bindsnet.git original
Cloning into 'original'...
  ...
(bindsnet) ~/aimldl/bindsnet$ ls
README.md  configure.md  original
```
Notice thta directory "original" is created.

#### 1.2.1. Installing the Required Packages from requirements.txt Fails!
Installing the required package with requirements.txt fails. Move onto the next section to see a valid command. This section explains the details why it didn't work.

```bash
(bindsnet) ~/aimldl/bindsnet$ cd original
(bindsnet) ~/aimldl/bindsnet/original$ pip install -r requirements.txt
```
Installing the required packages by the BindsNET authors fails with two errors:
1. ModuleNotFoundError: No module named 'keyring.util.escape'
2. ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/smmap'
Consider using the `--user` option or check the permissions.

The --user option fails.
```bash
(bindsnet) ~/aimldl/bindsnet/original$ pip install -r --user requirements.txt
```
Adding "sudo" in front seems to solve the second error, but the first error still remains.
```bash
(bindsnet) ~/aimldl/bindsnet/original$ sudo pip install -r requirements.txt
```

From [BindsNET > README.md > Getting started](https://github.com/BindsNET/bindsnet/blob/master/README.md), running an example script eth_mnist.py should work if the installation went well.
```bash
$ cd examples/mnist
$ python eth_mnist.py
Traceback (most recent call last):
  File "eth_mnist.py", line 5, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```
But the command spits out a missing module error after another.
```bash
ImportError: No module named torch
```

### 1.2. Solution
#### 1.2.1. Installed One-by-One Manually
So I installed one missing package after another and ended up installing most of the required packages. The only recognized packages are scipy, numpy,setuptools, and opencv-python. So I could conclude the rest of packages from requirements.txt are not installed properly.

Pytorch is installed according to https://anaconda.org/pytorch/pytorch.
```bash
$ conda install -c pytorch pytorch
```

```bash
$ pip install foolbox
$ pip install torchvision
$ pip install tqdm
$ pip install matplotlib
$ pip install gym
$ pip install scikit_image
$ pip install scikit_learn
$ pip install sphinx_rtd_theme
$ pip install pytest
$ pip install cython
$ pip install pandas
$ pip install tensorboardX
$ pip install pre-commit
```
(It's not important, but I aliased "pip install" to "pp".)

The bindsnet package was the last package to make eth_mnist.py run properly.
```bash
$ pip install pip install bindsnet
```
#### 1.2.2. Better to Use the Following Command
Putting together all the package names into one results in the following command.
```bash
$ conda install -c pytorch pytorch
$ pip install foolbox scipy numpy torch  torchvision tqdm setuptools matplotlib gym scikit_image scikit_learn opencv-python sphinx_rtd_theme pytest cython pandas tensorboardX pre-commit
$ pip install pip install bindsnet
```
### 1.3. Verification
After the installation is done, "$ python eth_mnist.py" runs properly as follows.
```bash
(bindsnet) ~/aimldl/bindsnet/original/examples/mnist$ python eth_mnist.py
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw/train-images-idx3-ubyte.gz
100%|████████████████████████████████████████████████████████▊| 9879552/9912422 [00:17<00:00, 570776.55it/s]Extracting ../../data/MNIST/TorchvisionDatasetWrapper/raw/train-images-idx3-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw/train-labels-idx1-ubyte.gz
32768it [00:00, 51419.41it/s]
Extracting ../../data/MNIST/TorchvisionDatasetWrapper/raw/train-labels-idx1-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw/t10k-images-idx3-ubyte.gz
                                                                                                           Extracting ../../data/MNIST/TorchvisionDatasetWrapper/raw/t10k-images-idx3-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw/t10k-labels-idx1-ubyte.gz
8192it [00:00, 22084.44it/s]
Extracting ../../data/MNIST/TorchvisionDatasetWrapper/raw/t10k-labels-idx1-ubyte.gz to ../../data/MNIST/TorchvisionDatasetWrapper/raw                                                          | 0/4542 [00:00<?, ?it/s]
Processing...
Done!

Begin training.

Progress: 0 / 1 (0.0000 seconds)
9920512it [00:30, 570776.55it/s]
All activity accuracy: 9.20 (last), 9.20 (average), 9.20 (best)
Proportion weighting accuracy: 9.20 (last), 9.20 (average), 9.20 (best) 250/60000 [00:50<3:18:58,  5.00it/s]


All activity accuracy: 32.00 (last), 20.60 (average), 32.00 (best)
Proportion weighting accuracy: 33.20 (last), 21.20 (average), 33.20 (best)0/60000 [01:42<3:26:46,  4.80it/s]
  ...

(bindsnet) ~/aimldl/bindsnet/original/examples/mnist$
```
### Appendix: Error 1-Full Message
```bash
Error initializing plugin EntryPoint('Windows (alt)', 'keyrings.alt.Windows', None, Distribution('keyrings.alt', '3.0')).
Traceback (most recent call last):
  File "/home/aimldl/.local/lib/python3.6/site-packages/keyring/backend.py", line 190, in _load_plugins
    init_func = ep.load()
  File "/home/aimldl/.local/lib/python3.6/site-packages/entrypoints.py", line 82, in load
    mod = import_module(self.module_name)
  File "/usr/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/usr/lib/python3/dist-packages/keyrings/alt/Windows.py", line 9, in <module>
    from . import file_base
  File "/usr/lib/python3/dist-packages/keyrings/alt/file_base.py", line 13, in <module>
    from keyring.util.escape import escape as escape_for_ini
ModuleNotFoundError: No module named 'keyring.util.escape'
Error initializing plugin EntryPoint('file', 'keyrings.alt.file', None, Distribution('keyrings.alt', '3.0')).
Traceback (most recent call last):
  File "/home/aimldl/.local/lib/python3.6/site-packages/keyring/backend.py", line 190, in _load_plugins
    init_func = ep.load()
  File "/home/aimldl/.local/lib/python3.6/site-packages/entrypoints.py", line 82, in load
    mod = import_module(self.module_name)
  File "/usr/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/usr/lib/python3/dist-packages/keyrings/alt/file.py", line 11, in <module>
    from keyring.util.escape import escape as escape_for_ini
ModuleNotFoundError: No module named 'keyring.util.escape'
Error initializing plugin EntryPoint('pyfs', 'keyrings.alt.pyfs', None, Distribution('keyrings.alt', '3.0')).
Traceback (most recent call last):
  File "/home/aimldl/.local/lib/python3.6/site-packages/keyring/backend.py", line 190, in _load_plugins
    init_func = ep.load()
  File "/home/aimldl/.local/lib/python3.6/site-packages/entrypoints.py", line 82, in load
    mod = import_module(self.module_name)
  File "/usr/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/usr/lib/python3/dist-packages/keyrings/alt/pyfs.py", line 8, in <module>
    from keyring.util.escape import escape as escape_for_ini
ModuleNotFoundError: No module named 'keyring.util.escape'
Collecting foolbox (from -r requirements.txt (line 1))
```

### Appendix: Error 2-Full Message
```bash
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/smmap'
Consider using the `--user` option or check the permissions.

Building wheels for collected packages: foolbox, gym, nodeenv, future
  Building wheel for foolbox (setup.py) ... done
  ...
Successfully built foolbox gym nodeenv future
Installing collected packages: smmap2, gitdb2, GitPython, foolbox, tqdm, future, pyglet, cloudpickle, opencv-python, gym, networkx, PyWavelets, scikit-image, sphinx-rtd-theme, py, more-itertools, zipp, importlib-metadata, pluggy, atomicwrites, pytest, cython, tensorboardX, virtualenv, importlib-resources, aspy.yaml, cfgv, nodeenv, toml, identify, pre-commit
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/smmap'
Consider using the `--user` option or check the permissions.

WARNING: You are using pip version 19.2.3, however version 19.3.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(bindsnet) aimldl@GPU-Desktop:~/aimldl/bindsnet/original$
```
(EOF)
