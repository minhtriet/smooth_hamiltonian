import pennylane as qml
import numpy as np


# Create a device
dev = qml.device("default.qubit", wires=1)

def smooth_function(x):
    assert -1 <= x <= 1
    return x**3


def get_ket(j, N):
    ket = np.zeros(N, dtype=complex)
    ket[j] = 1
    return ket

# Create a QNode
@qml.qnode(dev)
def circuit(A, f):
    """
    U(t) = exp(-Ht)
    """

    # np.polynomial.chebyshev.Chebyshev([1,2,3])

    # Given a hermitian matrix A and a smooth function f : [−1, 1] → R, ||A|| ≤ 1,

    # \phi_j   j=1...N
    N = 2   # dimension of subspace
    for j in range(N):   # (33)
        sum_aij_nonzero = 0
        for k in range(N):
            first_term = np.sqrt(np.conj(A[j][k]))*get_ket(k, N)
            second_term = np.sqrt(1-np.abs(A[j][k]))*get_ket(k+N, N)
            if A[j][k] != 0.:
                 sum_aij_nonzero += first_term + second_term
        get_ket(j, N) @ 1/np.sqrt(d)*sum_aij_nonzero   # (33)
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
A = [[0., 1.], [1., 0.]]
d = 2

# Execute the circuit
result = circuit(A, smooth_function)
