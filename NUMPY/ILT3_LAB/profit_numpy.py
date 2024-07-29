#calculate the profit made by a company using numpy

import numpy as np

revenue=np.array([10000,12000,11000,10500])
expenses=np.array([4000,5000,4500,4800])
c = np.subtract(revenue, expenses)
print("total profit is:",c)
