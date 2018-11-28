NetSquid Snippet Installation
=============================

There are the general installation instructions for [NetSquid snippet](https://netsquid.org/snippets) packages.

Installation
------------

For Python to be able to find the NetSquid snippet package it needs to be installed as a package or added to the `PYTHONPATH` environment variable.

### Install using pip

To install the package using pip run the following command in the repository root directory:

```shell
pip3 install --user .
```

The package can also be installed in editable mode by adding `--editable`: this links the installation to the files in this repository, allowing the installed package to be edited.

```shell
pip3 install --user --editable .
```

### Install without using pip

To install without pip run the following command in the repository root directory:

```shell
python3 setup.py install --user
```

### Install by adding to _PYTHONPATH_

Add this repository to your `PYTHONPATH` environment variable.
For example, in a bash shell do:

```shell
export PYTHONPATH=$PYTHONPATH:/path/to/this/repository
```

or add this line to your `$HOME/.bashrc`.

Running the tests
-----------------

To run all of the available unit tests run the following command in the repository root directory:

```shell
python3 setup.py test
```
