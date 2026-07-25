"""
Topics Covered:
1. reshape()
2. shape
3. Automatic Dimension (-1)
4. Reshape 1D to 2D
5. Reshape 1D to 3D
"""

import numpy as np

arr = np.arange(12)
print("Original Array: ")
print(arr)

# shape
print("Shape:",arr.shape)    # (12,) 1-D Array
print(type(arr.shape))       # tuple (12,) "," indicate only one value in tuple 

# reshape to (3,4)
arr2 = arr.reshape(3,4)
print("\nReshape (3,4):")
print(arr2)

# In reshaping total element must be same as 12
# It can be:- (1,12),(12,1),(2,6),(6,2),(3,4),(4,3)

# Automatic Dimension (-1)
arr3 = arr.reshape(3,-1)        # -1 = 12/3 = 4
print("\nReshape (3,-1):")
print(arr.reshape(3, -1))

arr3 = arr.reshape(4,-1)
print("\nReshape (4,-1):")
print(arr.reshape(4, -1))

arr3 = arr.reshape(-1,6)        # -1 = 12/6 = 2
print("\nReshape (-1,6):")
print(arr.reshape(-1,6))

# Python not allow this type of reshaping, Numpy confused which dimension to calculate
# arr3 = arr.reshape(-1,-1)
# print(arr3)

# Reshaping 1D into 3D
arr = np.arange(24)
print("Original 1-D Array: ")
print(arr, "\nDimensions:", arr.ndim)

arr3 = arr.reshape(2,3,4)
print("After Reshaping: ")
print(arr3)
