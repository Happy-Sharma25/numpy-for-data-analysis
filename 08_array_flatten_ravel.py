"""
Topics Covered:
1. flatten()
2. ravel()
3. Difference Between flatten() and ravel()
"""

import numpy as np

# flatten():- Sometimes you want to convert everything into a row
# flatten creates a copy of original array

arr = np.arange(12)

arr_original = arr.reshape(2,2,3)
print("\nReshape 1-D Array to 3-D ")
print(arr_original)

arr_flatten = arr_original.flatten()
print("\nFlattened Array:")
print(arr_flatten)

arr_flatten[0] = 100
print("\nAfter modifying flattened array:")
print(arr_flatten)

# flatten makes a copy and original remains intact

print("\nOriginal array remains unchanged:")
print(arr_original)    

# ravel():- Looks almost identical to the flatten
# ravel returns a view of the original copy

arr_ravel = arr_original.ravel()             
print("Ravelled Array : ",arr_ravel)

# Modify the ravel

arr_ravel[0] = 100
print("\nAfter modifying ravel():")
print("Ravelled Array : ",arr_ravel)

print("\nOriginal Changed:")
print(arr_original)

# flatten v/s ravel
arr = np.array([
    [1,2],
    [3,4]
])

# flatten()
# Original unchanged.
a = arr.flatten()
a[0] = 99
print("\nOriginal Array not changed: ")          
print(arr)

# ravel()
# Original changed.
b = arr.ravel()
b[0] = 99
print("\nOriginal Array changed: ") 
print(arr)          
