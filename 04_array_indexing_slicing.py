"""
Topics Covered:
1. Indexing
2. Accessing Elements in 1D, 2D, and 3D Arrays
3. Slicing
"""

# Import NumPy

import numpy as np

# 1-D Array Indexing

arr_1d = np.array([10, 20, 30, 40, 50])

print("1-D Array:")
print(arr_1d)

print("First Element:", arr_1d[0])
print("Last Element:", arr_1d[-1])

# 2-D Array Indexing

arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2-D Array:")
print(arr_2d)

print("First Row:", arr_2d[0])
print("Second Row:", arr_2d[1])

print("Element at Row 2, Column 3:", arr_2d[1, 2])
print("Element at Row 3, Column 1:", arr_2d[2, 0])

# 3-Dimensional Array

arr_3d = np.array([
    [[1,2,3],
    [4,5,6]],
    
    [[7,8,9],
    [10,11,12]]
])
print("3-D Array: ", arr_3d)

# Accessing First Block

print("Block 1:- \n",arr_3d[0])

# Access elements of block 1
print("Printing the rows of block 1")
print("Row 1",arr_3d[0][0])         # Block 1 row 1
print("Row 2",arr_3d[0][1])          # Block 1 row 2

# Access elements of block 1 and row 
print("Printing the element of block 1 and row 1")
print(arr_3d[0][0][0])          # Block 1 row 1 element 1
print(arr_3d[0][0][1])          # Block 1 row 1 element 2
print(arr_3d[0][0][2])          # Block 1 row 1 element 3

# Access elements of block 1 and row 2
print("Printing the element of block 1 and row 2")
print(arr_3d[0][1][0])          # Block 1 row 2 element 1
print(arr_3d[0][1][1])          # Block 1 row 2 element 2
print(arr_3d[0][1][2])          # Block 1 row 2 element 3

# Accessing Block 2
print("Block 2:- \n",arr_3d[1])

# Access elements of block 2
print("Printing the rows of block 2")
print("Row 1",arr_3d[1][0])         # Block 2 row 1
print("Row 2",arr_3d[1][1])          # Block 2 row 2

# Access elements of block 2 and row 1
print("Printing the element of block 2 and row 1")
print(arr_3d[1][0][0])          # Block 2 row 1 element 1
print(arr_3d[1][0][1])          # Block 2 row 1 element 2
print(arr_3d[1][0][2])          # Block 2 row 1 element 3

# Access elements of block 2 and row 2
print("Printing the element of block 2 and row 2")
print(arr_3d[1][1][0])          # Block 2 row 2 element 1
print(arr_3d[1][1][1])          # Block 2 row 2 element 2
print(arr_3d[1][1][2])          # Block 2 row 2 element 3

# Slicing
# 2-Dimension
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(arr.shape)  #(3,3)

print("\nFirst Row:")
print(arr[0])

# All the rows and column 0,1

print("\nFirst Two Columns:")
print(arr[:,0:2]) 

 # All the rows and column 2

print("\nFirst Two Columns:")
print(arr[:,1])  

# Last two rows only

print("\nLast Two Rows:")
print(arr_2d[1:])

# First two rows and two columns

print("\nFirst Two Rows and First Two Columns:")
print(arr_2d[0:2, 0:2])
