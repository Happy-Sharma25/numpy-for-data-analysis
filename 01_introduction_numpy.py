'''
Topics covered:
1. Importing NumPy
2. Creating Numpy Array
3. Array Attributes
4. 2D and 3D Arrays
'''

# Importing NumPy 
import numpy as np

# Creating a 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Check type
print(type(arr))

# Array dimensions
print(arr.ndim)

# Shape
print(arr.shape)

# Data type
print(arr.dtype)

# Size
print(arr.size)

# =========================================================

# 2-Dimensional Array
arr_2d = np.array([
    [1,2,3],
    [4,5,6]
])
print("\n2-D Array:")
print(arr_2d)
print("Dimensions:", arr_2d.ndim)
print("Shape:", arr_2d.shape)

# =========================================================

# 3-Dimensional Array
arr_3d = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])
print("3-D Array: ", arr_3d)
print("\n3-D Array:")
print(arr_3d)
print("Dimensions:", arr_3d.ndim)
print("Shape:", arr_3d.shape)
