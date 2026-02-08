#  Create one multidimensional array of shape (3,4,2) and perform
# indexing and slicing on it.

import numpy as np

# Create a 3D array of shape (3, 4, 2)
arr = np.arange(24).reshape(3, 4, 2)
print("Full array:\n", arr)

print("\nElement at index [1, 2, 0]:", arr[1, 2, 0])

print("\n2D slice at index 0:\n", arr[0])

print("\nFirst two blocks (axis 0):\n", arr[:2])

print("\nRows 1 to 3 from all blocks:\n", arr[:, 1:3, :])

print("\nLast column of last axis:\n", arr[:, :, 1])

