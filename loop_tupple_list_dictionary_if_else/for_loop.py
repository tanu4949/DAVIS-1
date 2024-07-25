#python program for printing numbers which are divisible by 10 and 7 using for loop
print("the number between 10 to 500 divisible by both 10 and 7")
for i in range(10,500):
    if(i%10==0 and i%7==0):
        print(i)

#python program for printing and counting numbers which are divisible by 3 using for loop
count=0
print("the numbers between 100 to 1000 which is even and divisible by 3")
for i in range(100,1000):
    if(i%2==0 and i%3==0):
        print(i,end=",")
        count=count=1
print("\n--------------------------------------")
print("the count is",count)

#python program for printing sum of numbers using for loop 
list1=[80,90,30,20,70,80,39,87]
sum=0
for x in list1:
    sum=sum+x
print("the sum of numbers in list",sum)
print("the avg of numbers in list",(sum/8))

