NetSquid Snippet Installation
=============================

These are the general installation instructions for [NetSquid snippet](https://netsquid.org/snippets) packages.

Installation
------------

For Python to be able to find the NetSquid snippet package it needs to be installed as a package or added to the `PYTHONPATH` environment variable.

### Install using pip

To install the package and its requirements using pip run the following command in the repository root directory:

```shell
make install
```

Note: To be able to install NetSquid and possibly other snippets on the netsquid server you need to provide your user name and password for the pypi server (*pypi.netsquid.org*); these match your forum credentials. You can store the user name and password in the environment variables NETSQUIDPYPI_USER and NETSQUIDPYPI_PWD, respectively, to prevent having to type them in manually during installation.

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

To run all of the available unit tests including the linter, run the following command in the repository root directory:

```shell
make verify
```
