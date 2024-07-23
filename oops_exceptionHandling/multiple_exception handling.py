#multiple  exception handling
print("line 1")
print("line 2")
print("line 3")
print("line 4")

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))

try:
    print(num1/num2)
    open("anudip.txt")
except ZeroDivisionError as e:
    print(e)
except FileNotFoundError as e:
    print(e)

print("line 5")
print("line 6")


try:
    print(num1/num2)
    open("anudip.txt")
except :
    print("something went wrong")
