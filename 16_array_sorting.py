"""
Topics Covered:
1. np.sort()
2. arr.sort()
3. Sorting 2-D Arrays
4. Sorting Along an Axis
5. Descending Order
6. np.argsort()
"""

import numpy as np
# -------------------------------------
# np.sort :-
# -------------------------------------
# Returns a new sorted array
# Numpy sorts in ascending order by default

arr = np.array([50,10,40,20,30])

print("Original Array:")
print(arr)

print("\nSorted Copy:")
print(np.sort(arr))

print("\nOriginal Array After np.sort():")
print(arr)

# -------------------------------------
# arr.sort():- Sort the original array in place
# -------------------------------------

arr = np.array([50,10,40,20,30])
arr.sort()
print("\nArray After arr.sort():")
print(arr)

arr_alpha = np.array(["a","f","b","g","c","h","d","e"])

print("\nArray of Alphabets : ", arr_alpha)
arr_alpha.sort()

print("\nArray After arr_alpha.sort():")
print(arr_alpha)

print("\nOriginal Array After arr_alpha.sort():")
print(arr_alpha)

# -------------------------------------
# Sorting 2-D array
# -------------------------------------

arr = np.array([[30,10,20],[60,40,50]])
print("\nOriginal 2-D Array:")
print(arr)

print("\nSort Each Row:")
print(np.sort(arr))

# -------------------------------------
# Sort each column independently
# -------------------------------------

arr = np.array([
    [5,9,1],
    [2,7,6]
])
print("\nOriginal Array:")
print(arr)

print("\nSort Each Column:")
print(np.sort(arr, axis=0))

# -------------------------------------
# Descending Order
# -------------------------------------
# Numpy by default sorts only in ascending order.

arr = np.array([40,10,50,20])

print("\nAscending Order:")
print(np.sort(arr))

print("\nDescending Order:")
print(np.sort(arr)[::-1])

# -------------------------------------
# np.argsort():- 
# -------------------------------------
# Instead of returning sorted values, it returns the indices that would sort the array.

arr = np.array([40,10,50,20])

print("\nIndices That Sort the Array:")
print(np.argsort(arr))
