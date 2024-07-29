#sorting in array using the sort function in numpy

import numpy as np
arr = np.array([3, 1, 2, 4, 5])
# Sort the array in ascending order (creates a new sorted array)
sorted_arr = np.sort(arr)
# Print the sorted array
print("Sorted array (ascending):", sorted_arr)
# Sort the array in descending order
sorted_arr_desc = np.sort(arr)[::-1]
print("Sorted array (descending):",sorted_arr_desc)
