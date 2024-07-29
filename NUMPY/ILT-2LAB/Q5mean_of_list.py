#find the mean of every NumPy array in the given list
import numpy as np

# List Initialization
Input = [np.array([3, 2, 8,9]),
         np.array([4,12,34,25,78]),
         np.array([23, 12, 67])]

# Output list initialization
Output = []

# using np.mean()
for i in range(len(Input)):
   Output.append(np.mean(Input[i]))

# Printing output
print(Output)
