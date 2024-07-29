#sorting in array using the sort function in numpy row-wise (axis=1)

import numpy as np
arr = np.array([[3, 1, 2],[4, 4, 5]])
# Sort the array in ascending order (creates a new sorted array)
sorted_arr = np.sort(arr,axis=1)
# Print the sorted array
print("Sorted array (ascending):", sorted_arr)
