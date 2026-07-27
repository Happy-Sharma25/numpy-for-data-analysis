"""
File: 02_numpy_array_creation.py

Topics Covered:
1. np.zeros()
2. np.ones()
"""

import numpy as np

# ==========================================
# np.zeros()
# Creates an array filled with zeros.
# Default data type is float.
# ==========================================

zeros_float = np.zeros((2, 3))
print("Zeros Array (float):")
print(zeros_float)
print("Shape:", zeros_float.shape)
print("Data Type:", zeros_float.dtype)

print()

zeros_int = np.zeros((2, 3), dtype=int)
print("Zeros Array (int):")
print(zeros_int)
print("Shape:", zeros_int.shape)
print("Data Type:", zeros_int.dtype)

# ==========================================
# np.ones()
# Creates an array filled with ones.
# Default data type is float.
# ==========================================

print()

ones_float = np.ones((2, 3))
print("Ones Array (float):")
print(ones_float)
print("Shape:", ones_float.shape)
print("Data Type:", ones_float.dtype)

print()

ones_int = np.ones((2, 3), dtype=int)
print("Ones Array (int):")
print(ones_int)
print("Shape:", ones_int.shape)
print("Data Type:", ones_int.dtype)
