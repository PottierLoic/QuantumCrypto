
import random
import math
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

n = 4

solution = random.randint(0, 2**n - 1)
print(f"Le mot de passe correct (en binaire) : {format(solution, '04b')}")

qc = QuantumCircuit(n)

qc.h(range(n))

oracle = QuantumCircuit(n)

for i in range(n):
    if solution & (1 << i) == 0:
        oracle.x(i)

oracle.h(n-1)
oracle.mcx(list(range(n-1)), n-1)
oracle.h(n-1)

for i in range(n):
    if solution & (1 << i) == 0:
        oracle.x(i)

diffusion = QuantumCircuit(n)
diffusion.h(range(n))
diffusion.x(range(n))
diffusion.h(n-1)
diffusion.mcx(list(range(n-1)), n-1)
diffusion.h(n-1)
diffusion.x(range(n))
diffusion.h(range(n))

num_iterations = 2
for _ in range(num_iterations):
    qc = qc.compose(oracle)
    qc = qc.compose(diffusion)

statevector = Statevector.from_instruction(qc)

probabilities = statevector.probabilities_dict()

plot_histogram(probabilities)
plt.show()

print("Résultats des probabilités :", probabilities)

