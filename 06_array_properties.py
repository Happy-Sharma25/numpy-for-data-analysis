"""
Topics Covered:
1. shape
2. ndim
3. size
4. dtype
"""

import numpy as np

# Array Properties:-

arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3-D Array: ", arr_3d)

# Shape:- gives the dimension of an array(block,row,column)
print("Dimension of array: ",arr_3d.shape)   #(2,2,3)
'''
├── Block 1
│   ├── Row 1 → [1, 2, 3]  ← 3 columns
│   └── Row 2 → [4, 5, 6]
│
└── Block 2
    ├── Row 1 → [7, 8, 9]
    └── Row 2 → [10,11,12]

2 blocks
2 rows per block
3 columns per row

'''
# ndim():- Gives the dimension of an array
print("Dimension of arr_3d : ",arr_3d.ndim)

# size():- Return the total number of elements
print("Number of elements in arr_3d : ", arr_3d.size)

# dtype():- Shows the data type of the elements.
print("Data type of elements : ",arr_3d.dtype)

