import math
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator
from qiskit.visualization import plot_distribution
from qiskit.primitives import Sampler

n = 4 
qc = QuantumCircuit(n)

qc.h(range(n))

oracle = QuantumCircuit(n)
oracle.x(range(n))
oracle.h(n - 1)
oracle.mcx(list(range(n - 1)), n - 1)
oracle.h(n - 1)
oracle.x(range(n))

grover_op = GroverOperator(oracle)

iterations = int(math.pi / 4 * math.sqrt(2**n))
for _ in range(iterations):
    qc = qc.compose(grover_op)

qc.measure_all()

sampler = Sampler()
job = sampler.run(qc)
result = job.result()

quasi_dist = result.quasi_dists[0]

plot_distribution(quasi_dist, title="Grover's Algorithm Results with 4 Qubits")

for i in range(2**n):
    binary_state = format(i, f'0{n}b')
    probability = quasi_dist.get(i, 0)
    print(f"State |{binary_state}>: {probability:.4f}")
