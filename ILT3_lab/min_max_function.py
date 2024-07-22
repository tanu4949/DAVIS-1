#Using max() and min() functions display the maximum and minimum of 5 random numbers.
import random
for random_number in range(0,5):
    random_number = random.randint(1, 20)
    lis1=[random_number]
    print(lis1)
    
print("the maximum of random numbers is",max(lis1))
print("the minimum of random numbers is",min(lis1))

