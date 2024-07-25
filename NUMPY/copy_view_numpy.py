#python program for using function copy() in numpy
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print("the original array",arr)
x=arr.copy()
arr[0]=42
print("after changing value at 0th index is in copied array:")
print(x)
print("-------------------------------------------------")
#python program for using function view() in numpy
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
x=arr.view()
arr[0]=42
print(arr)
print("after changing value at 0th index is in viewed array:")
print(x)
