import numpy as np

# Boolean :- # A Boolean value can only be True or False.

# Boolean Array

marks = np.array([45, 70, 90, 55, 80])
print("Marks grater than 60 : ")
print(marks > 60)
# Check whether elements are greater than 60: True_if_yes, False_if_no

# Boolean Filtering

# Print all the marks GREATER THAN 60
print(marks[marks > 60])     # [70 90 80]

# How Boolean Array Works

marks = np.array([45, 70, 90, 55, 80])
# First numpy calculate :
print(marks > 60)    # [False  True  True False  True]
# than only TRUE positions are selected
# [70 90 80]

# Print all the marks LESS THAN 60
print(marks[marks < 60])

# Print all the marks EQUAL to 70
print(marks[marks == 70])

# Print all the marks NOT EQUAL to 70
print(marks[marks != 70])

# Print all the marks GREATER THAN OR EQUAL
print(marks[marks >= 80])

# Multiple condition
# AND CONDITION

# Find student scoring between 60 and 85
print(marks[(marks>60) & (marks<85)])

# OR CONDITION

# Find marks if less than 50 or greater than 85
print(marks[(marks<50) | (marks>85)])

# NOT CONDITION

# Remove students scoring below 60
print(marks[~(marks<60)])

# ..................... Boolean Indexing .................

sales = np.array([[100,200,300],
                  [150,250,350],
                  [400,500,600]])

print(sales>250) 
'''             [[False False  True]
                [False False  True]
                [ True  True  True]]'''
print(sales[sales>250]) # Only TRUE positions are selected.
# [300 350 400 500 600]

# ........................... FILTERING ROWS ...................

# Both arrays must have the same number of elements so the Boolean mask aligns correctly.
salary = np.array([25000, 50000, 65000, 30000])
names = np.array(["Ram", "Mohan", "Rahul", "Amit"])
print(salary > 40000)
print(salary[salary>40000])
print("Name with Salary: ")
print(names[salary>40000]) # The mask lets you keep related arrays aligned.

# ............................. Replacing Values ......................

# Replace the values less than 60 with 60
marks = np.array([45, 70, 90, 55, 80])
# marks<60   prints: [True,False,False,True,False]
# marks[marks<60] = 45,50
marks[marks<60] = 60
print(marks)

# ........................... Counting Matches .................... 

# How many students passed?
marks = np.array([45, 70, 90, 55, 80])
print(np.sum(marks>=60))

# Suppose you have temperatures for a month.
temp = np.array([28, 31, 35, 40, 42, 29, 27, 38])

# Hot days
print(temp[temp>=35])

# Comfortable days
print(temp[(temp>=25) & (temp<=30)])

# Count Hot days
print(np.sum(temp>=35))

# Average hot day temperature
print(temp[temp>=35].mean())

'''
 ........................... Cheat Sheet ......................
 
 Task                            | Code                             |              |
 ------------------------------- | -------------------------------- | ------------ |
 Greater than 100                | `arr[arr > 100]`                 |              |
 Less than 50                    | `arr[arr < 50]`                  |              |
 Equal to 10                     | `arr[arr == 10]`                 |              |
 Not equal to 0                  | `arr[arr != 0]`                  |              |
 Between 20 and 50               | `arr[(arr >= 20) & (arr <= 50)]` |              |
 Less than 10 or greater than 90 | `arr[(arr < 10)                  | (arr > 90)]` |
 Replace negatives with 0        | `arr[arr < 0] = 0`               |              |
 Count values above 100          | `np.sum(arr > 100)`              |              |
'''
