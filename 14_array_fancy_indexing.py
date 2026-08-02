"""
Topics Covered:
1. Fancy Indexing
2. Selecting Multiple Elements
3. Selecting Multiple Rows
4. Selecting Multiple Columns
5. Reordering Rows
6. Boolean Fancy Indexing
"""

"""
Fancy Indexing :- 
Fancy indexing allows you to select multiple elements,rows or columns using a list.
"""

import numpy as np

# Select Multiple Elements
arr = np.array([10, 20, 30, 40, 50])
print("Array : ", arr)
print("Selecting multiple array using fancy indexing : ")
print(arr[[0, 2, 4]])

# Select Multiple Rows
data = np.array([
    [101, 25, 50000],
    [102, 30, 60000],
    [103, 28, 55000],
    [104, 35, 70000]
])
print("\nSelecting multiple rows from Array2 : \n", data)
print("\nresult : ")
print(data[[0, 2]])

# Select Multiple Columns

print("\nSelecting Multiple Column : ")
print(data[:, [0, 2]])

# Reorder Rows
print("\nReordering the rows : ")
print(data[[0,2,1,3]])

# Boolean Fancy Indexing
# Filter data based on conditions.
salary = np.array([30000, 50000, 45000, 60000])
print("\nBoolean Filteration : ")
print(salary[salary>45000])
