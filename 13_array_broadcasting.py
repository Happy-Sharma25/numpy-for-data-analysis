'''
BROADCASTING
Broadcasting allows NumPy to perform arithmetic operations
on arrays of different shapes without explicitly copying data.
'''

import numpy as np 

# Scalar Broadcasting

arr = np.array([10,20,30])
print("Scalar Broadcasting:")
print("\nArray1 : ", arr)
print("Adding 5 to all the elements of an array : ", arr + 5)

# Multiplication
arr = np.array([2,4,6])
print("\nArray2 : ", arr)
print("Multiply all the elements with 3 : ", arr*3)

# 1-D + 1-D
a = np.array([1,2,3])
b = np.array([10,20,30])
print("\nAdding two 1-D array: ", a , b)
print("Result : ", a+b)

# 2D + Scalar
arr3 = np.array([[1,2],
                [3,4]])
print("\nAdding a scalar value (5) to a 2-D array : \n", arr3)
print("Result : \n",arr3 + 5)

# Row Broadcasting

# Elements of rows in matrix array should be same in row matrix
matrix = np.array([[1,2,3],
                   [4,5,6]])
row = np.array([10,20,30])   # Shape (3,)  , Broadcasts across each row of the matrix
print("\nRow Broadcasting : ")
print(matrix + row)

# Column Broadcasting

# These two arrays are compatible for column broadcasting 
# as rows in matrix array = columns in column array
matrix = np.array([[1,2,3],
                   [4,5,6]])
column = np.array([[10],
                   [20]])
print("\nColumn Broadcasting : ")                   
print(matrix + column)
