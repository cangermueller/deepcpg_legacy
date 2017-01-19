DeepCpG
=======

Python package for predicting single-cell CpG methylation states from DNA
sequence and neighboring CpG sites using multi-task convolutional neural
networks.

**This repository is depracated. Please refer to the [new DeepCpG package](https://github.com/cangermueller/deepcpg)!**.

Installation
------------

The DeepCpG git repository can be checked out into the current directory by
executing the command

``git clone https://github.com/cangermueller/deepcpg.git``.

To install DeepCpG, execute `python setup.py install` in the root directory.

DeepCpG builds upon a fork of the deep learning framework
[Keras](http://keras.io/), which can be
installed by running the `setup.sh` script in the `tools/` directory, which will
checkout and install the repository.

Examples
--------
The `examples/` directory contains example scripts for training a small deep
neural network and predicting missing methylation states afterwards. The
necessary data sets can be downloaded by running `data.sh`. A network can be
trained by running `train.sh`, and methylation states for a test data set
be predicted by running `predict.sh`.


Content
-------
* `/deepcpg/`: DeepCpG package
* `/script/`: Scripts for data generation, model training, and imputation
* `/examples/`: Example files for model training and imputation
* `/data/`: Example data files

Contact
-------
* Christof Angermueller
* cangermueller@gmail.com
* https://cangermueller.com
