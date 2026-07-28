# Mathematical Operations

import numpy as np

sales = np.array([
    [120, 150, 180, 200],
    [100, 170, 190, 210],
    [130, 160, 170, 220]
])
print("Dataset: \n", sales)
print("\nShape of sales Dataset: ",sales.shape)       # (3,4)

# Sum():- Returns the total of all elements

# Sum of all the elements in an array:- 2000
print("\nSum of all the elements of sales Dataset: ",sales.sum())       

# Axis

# Sum of each columns, and return 1-D array.
print("\nSum of elements column wise: ",sales.sum(axis=0)) 

# Sum of each row, and return 1-D array.
print("\nSum of elements row wise: ",sales.sum(axis=1)) 

# Mean():- Returns the average

# Returns the average for all the elements.
print("\nAverage of overall sales Dataset: ",sales.mean())  

# Returns the average for individual columns.
print("\nColumn wise Average: ",sales.mean(axis=0)) 

# Returns the average for individual rows.
print("\nRow wise Average: ",sales.mean(axis=1)) 

# min():- Returns the smallest value

# Returns the smallest value in the array
print("\nSmallest Value in Dataset: ",sales.min())

# Returns the smallest value from individual column.
print("\nSmallest Value from every column: ",sales.min(axis=0))

# Returns the smallest value from individual row.
print("\nSmallest Value from every row: ",sales.min(axis=1)) 

# max():- Returns the Maximum value

# Returns the Maximum value in the array
print("\nMaximum Value in Array: ",sales.max())  

# Returns the Maximum value from in individual column.
print("\nMaximum Value in individual column: ",sales.max(axis=0)) 

# Returns the Maximum value from individual row.
print("\nMaximum Value in individual row: ",sales.max(axis=1)) 

# std():- Returns the Standard Deviation

# How much the numbers vary from the average.
print("\nStandard Deviation: ",sales.std())

# Size():- count the number of values/elements in an array.
print("\nSize of Array: ",sales.size)

# Median():- Middle value after sorting.
print("\nMedian: ",np.median(sales))

# Median when the array has an even number of elements.
profit = np.array([10, 20, 30, 40])
print("\nProfit Dataset: ",profit)
print("\nMedian if numbers are even(Profit Dataset): ",np.median(profit))            # (20+30)/2 = 25 if even elements.

# var():- Variance measures spread, and standard deviation is simply its square root:
print("\nVariance: ",sales.var())
