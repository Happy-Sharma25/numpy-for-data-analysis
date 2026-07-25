"""
Topics Covered:
1. NumPy Arrays are Mutable
2. Modify a Single Element
3. Modify an Entire Row
4. Modify an Entire Column
"""

import numpy as np

arr = np.array([10,20,30])
print("\nOriginal Array: ")
print(arr)

arr[1] = 99
print("\nArray after modify single element: ")
print(arr)

# Modify the entire row
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print("\nOriginal Array: ")
print(arr)

arr[0] = [10,20,30]
print("\nArray after modify entire row: ")
print(arr)

# Modify the entire column
arr[:,1] = 100
print("\nArray after modify entire column: ")
print(arr)
