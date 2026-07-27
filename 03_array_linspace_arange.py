"""
Topics Covered:
1. np.arange()
2. np.linspace()
"""

import numpy as np

# ==========================================
# np.arange()
# Creates an array with a fixed step size.
# Syntax: np.arange(start, stop, step)
# Note: The stop value is NOT included.
# ==========================================

arr = np.arange(10)
print("np.arange(10):")
print(arr)

print()

arr = np.arange(5, 10)
print("np.arange(5, 10):")
print(arr)

print()

arr = np.arange(2, 20, 2)
print("np.arange(2, 20, 2):")
print(arr)

print()

arr = np.arange(0, 1, 0.2)
print("np.arange(0, 1, 0.2):")
print(arr)


# ==========================================
# np.linspace()
# Creates evenly spaced values.
# Syntax: np.linspace(start, stop, num)
# Note: The stop value IS included.
# ==========================================

print()

arr = np.linspace(0, 10, 5)
print("np.linspace(0, 10, 5):")
print(arr)

print()

arr = np.linspace(1, 100, 10)
print("np.linspace(1, 100, 10):")
print(arr)
