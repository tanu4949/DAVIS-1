#find indices where the elements are 3
import numpy as np
arr=np.array([1,2,3,4,5])
indices=np.where(arr>3)
print(indices)
