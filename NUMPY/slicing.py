#python program for slicing and assigning values in array
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
sarr=arr[1:5]
print(arr)
print(sarr)
sarr[2]=100
print(arr)
print(sarr)
