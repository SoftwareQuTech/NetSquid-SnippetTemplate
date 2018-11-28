# This is an example module file with an associated unit test.
# You should replace these files with your own content.
#
# We suggest you use Numpy style docstrings in case your work could be integrated
# into NetSquid in the future:
# https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
"""Sample module for the snippet template.

Replace this with your own module(s).

"""
import netsquid as ns
import netsquid.qubits.qubitapi as qapi


def create_ghz_qubits(num_qubits):
    """Create qubits in a GHZ state.

    Parameters
    ----------
    num_qubits : int
        Number of qubits to return GHZ state for.

    Returns
    -------
    list of :obj:`~netsquid.qubits.qubit.Qubit`
        Qubits in a shared GHZ state.

    Notes
    -----
        This is just an example function for this sample module.

    """
    if not isinstance(num_qubits, int):
        raise TypeError("{} is not an integer".format(num_qubits))
    if num_qubits < 2:
        raise ValueError("Too few qubits to create GHZ state")
    qubits = qapi.create_qubits(num_qubits)
    qapi.operate(qubits[0], ns.H)
    for i in range(num_qubits - 1):
        qapi.operate(qubits[i:i+2], ns.CNOT)
    return qubits
