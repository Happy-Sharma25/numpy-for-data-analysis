# np.split(): It splits an array into equal-sized parts.
# np.split(array,indices_or_section,axis=0)

'''
array → Input array

indices_or_sections
Integer → Split into equal parts
List → Split at specific indices

axis
0 → Split rows
1 → Split columns
'''

import numpy as np
# 1-D array

arr = np.array([10,20,30,40,50,60])
result = np.split(arr,3)
print(result)

# split at specific indices
result = np.split(arr,[2,5])
print(result)
'''
The list [2,5] means:
First split before index 2
Second split before index 5
'''

# 2-D array
arr = np.array([[1,2],
                [3,4],
                [5,6],
                [7,8]])
print(arr)

# split rows
result = np.split(arr,2)
print(result)

# split column
result = np.split(arr,2,axis=1)
print(result)

# np.vsplit() :- vertical split

arr = np.array([[1,2],
                [3,4],
                [5,6],
                [7,8]])
result = np.vsplit(arr,2)
print(result)

arr = np.arange(16).reshape(4,4)
print(arr)

# split into four parts
print(np.vsplit(arr,4))

# np.hsplit():- Horizontal Split
# splits column EQUIVALENT to np.split(arr,....,axis=1)
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

# split into two parts
result = np.hsplit(arr,2)
print(result)

# splits every column seperately
print(np.hsplit(arr,4))

# splits at specific column
arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(np.hsplit(arr,[2,4]))
