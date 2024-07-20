count=0
print("the numbers between 100 to 1000 which is even and divisible by 3 ")
#using while loop
i=100
while(i<1000):
    if(i%2==0 and i%3==0):
        print(i,end=",")
        count=count=1
print("\n--------------------------------------")
print("the count is",count)
