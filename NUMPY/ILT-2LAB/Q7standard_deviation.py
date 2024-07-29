#Compute the standard deviation of the NumPy array

import numpy as np
arr= np.array([20, 2, 7, 1, 34])
arr_average=np.mean(arr)
print('array average',arr_average)
arr_std=np.std(arr)
print("the standard deviation ",arr_std)
print("more precision with float 32\n", np.float32(arr_std))
print("more accuracy with float 64\n", np.float64(arr_std))
