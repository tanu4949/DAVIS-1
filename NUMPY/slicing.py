#python program for slicing and assigning values in array
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
sarr=arr[1:5]
print(arr)
print(sarr)
sarr[2]=100
print(arr)
print(sarr)

#slicing in array and type
import numpy as n
arr=n.array([1,20,5,9,3,4,8,5,6,2,25,2,2265,3,33])
slicing=arr[4:9]
print("new slicing",slicing)
print("new array",arr)
print(type(slicing))
print(type(arr))
slicing[:]=0
print("new slicing",slicing)
print("new array",arr)
