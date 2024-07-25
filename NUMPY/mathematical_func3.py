#python program for performing mathematical functions on the array
import numpy as n
n.random.seed(122)
mat=n.random.randint(1,21,9).reshape(3,3)
print(mat)
print("the sum of whole array",n.sum(mat))
print("the cumulative sum of whole array",n.cumsum(mat))
print("the minimum in whole array",n.min(mat))
print("the maximum in whole array",n.max(mat))
print("--------------------------------------------------")
print("the sum of 1st row,2nd row ,3rd row array",n.sum(mat,axis=1))
print("the cumulative sum of rows of  array",n.cumsum(mat,axis=1))
print("the minimum in all rows in array",n.min(mat,axis=1))
print("the maximum in all rows in array",n.max(mat,axis=1))
print("--------------------------------------------------")
print("the sum of all column array",n.sum(mat,axis=0))
print("the cumulative sum of columns of  array",n.cumsum(mat,axis=0))
print("the minimum in all columns in array",n.min(mat,axis=0))
print("the maximum in all columns in array",n.max(mat,axis=0))
