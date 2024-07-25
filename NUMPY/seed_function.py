# using the seed function so that we can get the same random number
import numpy as n
n.random.seed(125) #use same number
arr=n.random.randint(1,100,12)
print(arr)

# using the seed function so that we can get the same random number
import numpy as n
n.random.seed(111)
arr=n.random.randint(1,500,30).reshape(6,5)
print(arr)
print(arr[2:,2:])
print(arr[3:5,2:4])
