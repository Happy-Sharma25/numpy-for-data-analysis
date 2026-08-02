"""
Topics Covered:
1. np.random.rand()
2. np.random.randn()
3. np.random.randint()
4. np.random.seed()
5. np.random.choice()
"""

import numpy as np

# np.random.rand():- Generates RANDOM DECIMAL NUMBERS b/w 0 and 1
print("Random Decimal Number:")
print(np.random.rand())

# 5 random decimal number
print("\nFive Random Decimal Numbers:")
print(np.random.rand(5))

# Random 2-D array
# There are 8 numbers after decimal, to reduce these we use ROUND function

# Reduce decimal number to 2
print("\nRandom 2-D Array:")
arr = np.random.rand(3, 4)
print(np.round(arr, 2))

# np.random.randn():- Generate random positive and negative numbers
print("\nFive Random Numbers (Normal Distribution):")
print(np.random.randn(5))

print("\nRandom 2-D Array (Normal Distribution):")
arr = np.random.randn(3,4)
print(np.round(arr,2))

# np.random.randint():- Generate random integers
# Generates integer from 1 to 9 (10 is excluded)
print("\nRandom Integer:")
print(np.random.randint(1, 10))

# Generate mutiple values (5)
print("\nFive Random Integers:")
print(np.random.randint(1, 10, 5))

# Generate a matrix of (3,4)
print("\nRandom Integer Matrix:")
print(np.random.randint(50, 100, (3, 4)))

# np.random.seed();- Makes random number repeatable
np.random.seed(39)
print("\nRandom Numbers Using Seed:")
print(np.random.randint(1, 10, 5))
# If someone else runs the same code with the same seed, they get the same result.

# np.random.choice():- Randomly selects values from a list or array.

colors = ["Red","Blue","Green","Black"]

print("\nRandom Color:")
print(np.random.choice(colors))

# select multiple values (3)
print("\nThree Random Colors:")
print(np.random.choice(colors, 3))

# without duplicates 
print("\nThree Unique Random Colors:")
print(np.random.choice(colors, 3, replace=False))
