#determine which product  in a store is out of stock(quantity=0)
import numpy as np
product=np.array([10,0,0,20,0])
d= product[product==0]
print("the product which are out of stock are",d)
