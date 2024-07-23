#single exception handling
print("line 1")
print("line 2")
print("line 3")
print("line 4")

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))

try:
    print(num1/num2)
    print("inside a try")
except ZeroDivisionError as e:
    e="not divisible by 0"
    print(e)

    
print("line 5")
print("line 6")
