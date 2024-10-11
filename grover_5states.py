import math
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
from qiskit import transpile
import matplotlib.pyplot as plt

n = 5
N = 2**n
iterations = int(math.sqrt(N))

qc = QuantumCircuit(n, n)

qc.h(range(n))

# Oracle that marks the state |11111>
oracle = QuantumCircuit(n)
oracle.mcx(list(range(n - 1)), n - 1)

grover_op = GroverOperator(oracle)

for _ in range(iterations):
  qc = qc.compose(grover_op)

qc.measure(range(n), range(n))

simulator = AerSimulator()
qc = transpile(qc, simulator)
job = simulator.run(qc, shots=1000)
result = job.result()

counts = result.get_counts()

plot_histogram(counts, title="Grover's Algorithm Results with 5 Qubits")
plt.show()

for state, count in counts.items():
  print(f"State |{state}>: {count / 1000:.4f}")
