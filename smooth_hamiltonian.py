import pennylane as qml
import numpy as np


# Create a device
dev = qml.device("default.qubit", wires=1)

# Create a QNode
@qml.qnode(dev)
def circuit(A):
    """
    U(t) = exp(-Ht)
    """

    # np.polynomial.chebyshev.Chebyshev([1,2,3])

    # Given a hermitian matrix A and a smooth function f : [−1, 1] → R, ||A|| ≤ 1,

    # \phi_j
    #  j=1...N
    #
    # define isometry T from phi some multi swap operator(3 rd ingredient),
    #
    # can be replaced with multiple swap gates S define W from S and T  (36)

    # H = A/d, d is the d-sparse Hermitian matrix
    #

    # Call W() to define the quantum walk (13)

    # LCU
    # Now we have Chebyshev series

    # TODO NExt step (6.2),


    return qml.states()

def W(_lambda: float,  ):
    # define coeff
    # define T, and U
    pass

# Initialize parameters

# Execute the circuit
result = circuit()
