import pennylane as qml
import numpy as np

# np.polynomial.chebyshev.Chebyshev([1,2,3])

# Create a device
dev = qml.device("default.qubit", wires=1)

# Create a QNode
@qml.qnode(dev)
def circuit(params):
    return qml.states()

# Initialize parameters

# Execute the circuit
result = circuit()
