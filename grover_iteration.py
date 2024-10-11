import numpy as np
from qutip import *

zero = basis(2, 0)
one = basis(2, 1)
initial_state = tensor(zero, zero)

H = (1/np.sqrt(2)) * Qobj([[1, 1], [1, -1]])
H2 = tensor(H, H)

state = H2 * initial_state

oracle_matrix = np.eye(4)
oracle_matrix[3, 3] = -1
oracle = Qobj(oracle_matrix, dims=[[2, 2], [2, 2]])
state = oracle * state

initial_state_projector = initial_state * initial_state.dag()
identity_matrix = qeye([2, 2])
diffusion_matrix = 2 * initial_state_projector - identity_matrix
diffusion = Qobj(diffusion_matrix, dims=[[2, 2], [2, 2]])

state = diffusion * state
state = H2 * state
final_state = state.ptrace([0, 1])
probabilities = np.abs(state.full())**2

print("Probabilities for measuring |00>, |01>, |10>, |11>:")
print(probabilities)