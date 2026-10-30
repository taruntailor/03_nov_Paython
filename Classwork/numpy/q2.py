import numpy as np

matrix = np.random.randint(1, 21, size=(4, 4))
print(matrix)

matrix[matrix < 15] += 10
print(" matrix:\n", matrix)

[matrix % 3 == 0] *= 2
print(" matrix:\n", matrix)
