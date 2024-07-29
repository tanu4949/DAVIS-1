#calculate the total cost of items in a shopping cart,considering the price per item

import numpy as np
quantity=np.array([2,3,4,1])
price_item=np.array([10.0,5.0,8.0,12.0])
c = np.multiply(quantity,price_item)
print("total cost of items is:",c)
