#create an multi dimentioal array of ones and zeros with elements and integer with datatype using "eye" function
import numpy as n
arr=(3,4)
arr2=n.eye(arr)
print(arr2)

#to fetch diagonal elements in the array

import numpy as n
arr=n.array([[1,2,3],[4,5,6],[4,5,6]])
print(n.diag(arr))
