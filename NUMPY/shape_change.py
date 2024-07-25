#changing the shape of an array
import numpy as np
arr=np.array([1,2,3,4,5,50])
print(arr)
arr.reshape(3,2)
print(arr)

# changing the shape of array
import numpy as np
arr=np.random.randint(0,100,12)
print(arr)
arr=arr.reshape(4,3)
print(arr)
print("array values is",arr[0][1])
print("array values is",arr[1][0])
print(arr.shape)
arr=arr.reshape(-1,4)
print(arr)
arr=arr.reshape(2,-1)
print(arr)
