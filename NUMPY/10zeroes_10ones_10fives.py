#write a numpy program to create array of 10 zeroes, 10 ones, and 10 fives.

import numpy as np

# Step 1: Create arrays of 10 zeros, 10 ones, and 10 fives
zeros_array = np.zeros(10, dtype=int)
print("the array with 10 zeroes",zeros_array)
ones_array = np.ones(10, dtype=int)
print("the array with 10 ones",ones_array)
fives_array = np.full(10, 5, dtype=int)
print("the array with 10 fives",fives_array)




