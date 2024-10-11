from qiskit_aer import AerSimulator
from qiskit.primitives import Sampler
from qiskit_algorithms import Shor

# Use AerSimulator
backend = AerSimulator()

# Create a Sampler
sampler = Sampler()

# Shor's algorithm
shor = Shor(sampler=sampler)
result = shor.factor(15)

# Display the results
print(f"The factors are {result.factors}")