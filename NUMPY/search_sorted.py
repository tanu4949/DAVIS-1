#implementing the search sorted function for checking at which index the number should be added for maintaining sorted array
import numpy as np
arr=np.array([1,2,3,4,5])
indice= np.searchsorted(arr,7)
print(indice)
