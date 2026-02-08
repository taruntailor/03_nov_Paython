# 6. Create two 2d array and perform hstack and vstack.
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

h_stack = np.hstack((a, b))
print("Horizontal Stack:\n", h_stack)

v_stack = np.vstack((a, b))
print("\nVertical Stack:\n", v_stack)
