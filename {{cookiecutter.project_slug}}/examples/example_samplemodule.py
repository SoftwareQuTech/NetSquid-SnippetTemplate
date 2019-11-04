from {{ cookiecutter.project_folder }}.samplemodule import create_ghz_qubits


def main(no_output=False):
    # Create 3 qubits in a GHZ state
    qubits = create_ghz_qubits(3)

    # Check their state
    if not no_output:
        print(qubits[0].qstate)
