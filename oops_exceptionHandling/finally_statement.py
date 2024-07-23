#else and finally statement
print("line 1")
print("line 2")
print("line 3")
print("line 4")

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))

try:
    print(num1/num2)
except:
    print("something went wrong")
else: 
    print("else block")

finally:
    print("finally block")

print("line 5")
print("line 6")
