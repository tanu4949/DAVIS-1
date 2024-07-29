#python program for filtering item based on multiple conditions using numpy

import numpy as np
# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])
# Create a boolean mask based on a condition (e.g., values greater than 3)
mask = (arr > 3)
# Use the mask to filter elements in the array
filtered_array = arr[mask]
# Print the filtered array
print("Filtered Array:", filtered_array)
