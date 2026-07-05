##### aimldl > bindsnet > README.md
* Draft: 2019-11-19 (Mon)
# BindsNET
This repository is to study BindsNET. Refer to the original github repository https://github.com/BindsNET/bindsnet for more information.

## 1. Configuration
### 1.1. Set Up the Computing Environment
Configure the computing environment as described in [configure.md](#configure.md). Refer to [troubleshooting.md](#troubleshooting.md) if you're interested in how the errors are fixed during the installation process. The following commands are the summary of [configure.md](#configure.md) and [troubleshooting.md](#troubleshooting.md).
#### 1.1.1. Create a Conda Virtual Environment
```bash
(base) $ conda update -n base -c defaults conda
(base) $ conda create -n bindsnet
(base) $ conda activate bindsnet
(bindsnet) $
```
From now on, it's assumed you're in the "bindsnet" virtual environment.

#### 1.1.2. Install PyTorch and Required Python Packages
```bash
(bindsnet) $ conda install -c pytorch pytorch
(bindsnet) $ pip install foolbox scipy numpy torch torchvision tqdm setuptools matplotlib gym scikit_image scikit_learn opencv-python sphinx_rtd_theme pytest cython pandas tensorboardX pre-commit
(bindsnet) $ pip install pip install bindsnet
```

#### 1.1.3. Clone This Repository
```bash
(bindsnet) $ git clone https://github.com/aimldl/bindsnet.git
```

#### 1.1.4. cd into the Download Repository
"ls" shows directory bindsnet. cd into the directory to check the cloned result.
```bash
(bindsnet) $ cd bindsnet
```

```bash
(bindsnet) $ ls
bindsnet  ...
(bindsnet) $ cd bindsnet/
(bindsnet) $ ls
README.md  configure.md  original  troubleshooting.md
```
Directory original has the following directory structure.
```bash
(bindsnet) $ tree -d
.
├── bindsnet
│   ├── analysis
│   ├── conversion
│   ├── datasets
│   ├── encoding
│   ├── environment
│   ├── evaluation
│   ├── learning
│   ├── models
│   ├── network
│   ├── pipeline
│   └── preprocessing
├── docs
│   └── source
│       └── guide
├── examples
│   ├── benchmark
│   ├── breakout
│   ├── mnist
│   └── tensorboard
└── test
    ├── analysis
    ├── conversion
    ├── encoding
    ├── import
    ├── models
    └── network
```

## 2. Getting started
Go back the original repository's "Getting started" and run:
```bash
(bindsnet) $ cd examples/mnist
(bindsnet) $ python eth_mnist.py
```
The MNIST example is like a hello world example for a programming language. If eth_mnist.py runs properly, it's ready to get started.

Directory "examples/mnist" has the following Python scripts.
```bash
$ tree examples/mnist/
examples/mnist/
├── batch_eth_mnist.py
├── conv_mnist.py
├── eth_mnist.py
├── reservoir.py
└── supervised_mnist.py
```

(EOF)
