# This file uses NumPy style docstrings: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

"""Unit tests for the sample module.

This file will be discovered by ``python setup.py test``.

"""
import pytest
import numpy as np
from netsquid.qubits.ketstates import s0, s1, s00, s11, b00
from netsquid.qubits.qubitapi import fidelity
from {{ cookiecutter.project_folder }}.samplemodule import create_ghz_qubits


@pytest.mark.parametrize("num_qubits, expected_state", [
    (2, b00),
    (3, (np.kron(s0, s00) + np.kron(s1, s11)) / np.sqrt(2)),
    (4, (np.kron(s00, s00) + np.kron(s11, s11)) / np.sqrt(2)),
])
def test_create_ghz_state(num_qubits, expected_state):
    """Test creation of GHZ states."""
    qubits = create_ghz_qubits(num_qubits)
    assert fidelity(qubits, expected_state) == pytest.approx(1.)


@pytest.mark.parametrize("num_qubits, expected_error", [
    (3., TypeError),
    ("3", TypeError),
    (0, ValueError),
    (1, ValueError),
])
def test_faulty(num_qubits, expected_error):
    with pytest.raises(expected_error):
        create_ghz_qubits(num_qubits)
