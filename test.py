import pennylane as qml

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def two_close_spins_X(B, J, time, n):
    """Circuit for evolving the state of two electrons with an X coupling.

    Args:
        B (float): The strength of the field, assumed to point in the z direction.
        J (float): The strength of the coupling between electrons.
        time (float): The time we evolve the electron wavefunction for.
        n (int): The number of steps in our Trotterization.

    Returns:
        array[complex]: The quantum state after evolution.
    """
    e = 1.6e-19
    m_e = 9.1e-31
    alpha = B * e / (2 * m_e)
    hbar = 1e-34
    beta = -J * hbar / 4
    ##################
    # YOUR CODE HERE #
    ##################
    for i in range(n):
        qml.PauliRot(-beta * time / n * 2, 'XX', [0, 1])
        qml.PauliRot(-alpha * time / n * 2, 'Z', 0)
        qml.PauliRot(-alpha * time / n * 2, 'Z', 1)

    return qml.state()

print(two_close_spins_X(1, 1, 3, 100))