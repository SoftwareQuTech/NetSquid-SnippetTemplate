# This file uses NumPy style docstrings: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

"""Unit tests for the sample module.

This file will be discovered by ``python setup.py test``.

"""
import unittest
import numpy as np
from netsquid.qubits.ketstates import s0, s1, s00, s11, b00
from netsquid.qubits.qubitapi import fidelity
from netsquid_mysnippet.samplemodule import create_ghz_qubits


class TestSampleModule(unittest.TestCase):
    """Unit tests for the sample module.

    Test methods should begin with 'test'.

    """
    def setUp(self):
        # Peform setup steps before each test
        self.ghz2 = b00
        self.ghz3 = (np.kron(s0, s00) + np.kron(s1, s11)) / np.sqrt(2)
        self.ghz4 = (np.kron(s00, s00) + np.kron(s11, s11)) / np.sqrt(2)

    def tearDown(self):
        # Peform tear down steps after each test
        pass

    def test_create_ghz_state(self):
        """Test creation of GHZ states."""
        for n, ket in zip(range(2, 4), [self.ghz2, self.ghz3, self.ghz4]):
            qubits = create_ghz_qubits(n)
            self.assertAlmostEqual(fidelity(qubits, ket), 1.)


if __name__ == "__main__":
    unittest.main(verbosity=2)
