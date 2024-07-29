#splitting of array using split() function

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
# Split the array into 3 equal-sized sub-arrays
sub_arr = np.split(arr, 3) #no.of array=3
# Print the sub-arrays
for sub_arr in sub_arr:
  print(sub_arr)
