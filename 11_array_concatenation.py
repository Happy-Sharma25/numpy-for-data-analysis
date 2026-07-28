"""
Topics Covered:
1. np.concatenate()
2. np.vstack()
3. np.hstack()
4. np.column_stack()
5. np.row_stack()
"""

import numpy as np

# 1-D array

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.concatenate((a,b))
print("Concatenate a, b :")
print(result)

# 2-D array ROW/COLUMN WISE
# All the rows are concatenate

x = np.array([[1, 2],
              [3, 4]])

y = np.array([[5, 6],
              [7, 8]]) 

print("\nAxis = 0  ↓  (Rows / Vertical direction)")
result = np.concatenate((x,y),axis=0)
print("Concatenate (axis=0):")
print(result)

print("\nAxis = 1  →  (Columns / Horizontal direction)")
result = np.concatenate((x,y),axis=1)
print("Concatenate (axis=1):")
print(result)

# =========================
# Vertical Stack (vstack)
# =========================

# It stacks arrays from top to bottom
# It is equivalent to  Row wise concatenate,np.concatenate((_,_),axis=0)

# 1-D array

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.vstack((a,b))
print("\nVertical Stacking applied on 1-D Array","\na : ",a,"\nb : ",b)
print("Result : \n",result)

# A 1-D array is treated as a single row during vertical stacking.
arr1 = np.array([[1, 2],
              [3, 4]])

arr2 = np.array([5, 6])  

print("\nOperation performed on these arrays:")
print("arr1:\n", arr1)
print("arr2:\n", arr2)
result = np.vstack((arr1,arr2))
print("\nResult\n",result)

# =========================
# Horizontal Stack (hstack)
# =========================

# Joins array side by side

# 1-D array

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nHorizontal Stack of 1-D Array a and b : ")
result = np.hstack((a,b))
print(result)

# 2-D array

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("\nHorizontal Stack of 2-D Array a and b : ")
print(np.hstack((a,b)))   
'''# visual: 1 2 | 5 6
             3 4 | 7 8     '''

# np.column_stack()

ages = np.array([22, 35, 30])
salary = np.array([40000, 50000, 60000])
print("\nColumn Stack operation performed on array: ",ages,"and",salary)
result = np.column_stack((ages,salary))
print("Result: \n", result)

# np.row_stack()

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# result = np.row_stack((a,b))
# print(result)
