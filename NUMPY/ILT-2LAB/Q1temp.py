#Suppose you have a dataset containing daily temperature readings for a city, and you
#want to identify days with extreme temperature conditions. Find days where the
#temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees
#Celsius (cold day).


from tabulate import tabulate

arr = np.array([32.5,34.2,36.8,29.3,31.0,38.7,23.1,18.5,22.8,37.2,4.0,5.5,9.0,-4.0,-12.0])
mask = (arr > 35)
# Use the mask to filter elements in the array
filtered_array = arr[mask]
 
# assign data
mydata1 = [["3","36.8"],["6","38.7"],["10","37.2"]]
print("hot day")
# create header
head = ["day", "temperature"]
# display table
print(tabulate(mydata1, headers=head))

print("cold day")
mydata2 = [["11","4.0"],["14","-4.0"],["15","-12.0"]]
mask1 = (arr < 5)
filtered_array = arr[mask1]
head = ["day", "temperature"]
print(tabulate(mydata2, headers=head))
