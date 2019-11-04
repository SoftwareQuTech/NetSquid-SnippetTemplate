Installation
------------

For Python to be able to find the NetSquid snippet package it needs to be installed as a package or added to the `PYTHONPATH` environment variable.

Install using pip
"""""""""""""""""

To install the package using pip run the following command in the repository root directory:

.. code-block:: shell

   make install

Note: If your snippet depends on other snippets on the netsquid server you first need to install them as

.. code-block:: shell

   pip3 install -r requirements.txt --extra-index-url https://<username>:<password>@pypi.netsquid.org

Install without using pip
"""""""""""""""""""""""""""""

To install without pip run the following command in the repository root directory:

.. code-block:: shell

   python3 setup.py install --user

Install by adding to _PYTHONPATH_
"""""""""""""""""""""""""""""""""

Add this repository to your `PYTHONPATH` environment variable.
For example, in a bash shell do:

.. code-block:: shell

   export PYTHONPATH=$PYTHONPATH:/path/to/this/repository

or add this line to your `$HOME/.bashrc`.

Running the tests
"""""""""""""""""

To run all of the available unit tests including the linter, run the following command in the repository root directory:

.. code-block:: shell

   make verify
