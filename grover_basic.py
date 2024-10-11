import math
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator
from qiskit.visualization import plot_distribution
from qiskit_aer import AerSimulator
from qiskit.primitives import Sampler

n = 2
qc = QuantumCircuit(n)

qc.h(range(n))

oracle = QuantumCircuit(n)
oracle.cz(0, 1)

grover_op = GroverOperator(oracle)
qc = qc.compose(grover_op)

qc.measure_all()

backend = AerSimulator()
sampler = Sampler()

job = sampler.run(qc, shots=1000)
result = job.result()

quasi_dist = result.quasi_dists[0]

plot_distribution(quasi_dist, title="Grover's Algorithm Results")

for i in range(4):
  binary_state = format(i, f'0{n}b')
  probability = quasi_dist.get(i, 0)
  print(f"State |{binary_state}>: {probability:.4f}")
