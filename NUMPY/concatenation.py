#concatenating along rows (vertical concatenation):

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6],[3,7]])
# Concatenate arr1 and arr2 along rows (vertical)
result = np.concatenate((arr1, arr2), axis=0)
# Print the concatenated array
print(result)



#concatenating along columns (horizontal concatenation):

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6],[3,6]])
# Concatenate arr1 and arr2 along columns (horizontal)
result = np.concatenate((arr1, arr2), axis=1)
# Print the concatenated array
print(result)
