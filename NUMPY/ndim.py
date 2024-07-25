#python program for using function ndim() for finding no.of dimensions

import numpy as np

a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]])

print("a array is",a)
print("b array is",b)
print("c array is",c)
print("d array is",d)


print("a array dimen",a.ndim)
print("b array dimen",b.ndim)
print("c array dimen",c.ndim)
print("d array dimen",d.ndim)
