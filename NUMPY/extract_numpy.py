#extracting the elements(only elements)
import numpy as np
arr=np.array([1,2,3,4,5])
indices=np.extract(arr>3,arr)
print(indices)
