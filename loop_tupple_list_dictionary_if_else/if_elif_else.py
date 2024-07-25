#PYTHON PROGRAM FOR FINDING OUT THE LARGEST NUMBER BETWEEN 2 NO.

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
if(num1==num2):
    print("they are equal")
elif (num1>num2):
  print(num1,"is greater")
else:
  print(num2,"is greater")




#PYTHON PROGRAM FOR FINDING OUT THE PROFIT AND LOSS

cost_price=float(input("Enter the cost Price of an Item :"))
selling_price=float(input("Enter the Selling Price of an Item :"))
if(selling_price<0)and (cost_price<0):
    print("both are invalid price")
elif(cost_price<0):
    print("invalid cost price")
elif(selling_price<0):
    print("invalid selling price")
else:
    if(selling_price > cost_price):
        profit = selling_price - cost_price
        print("Profit :",profit)
    elif( cost_price > selling_price):
        loss = cost_price - selling_price
        print("Loss :",loss)
    else:
        print("No Profit No Loss")



#PYTHON PROGRAM FOR TAKING INPUT AS SECONDS AND CONVERTING THEM INTO HOURS,MINUTES,AND SECONDS 

seconds = 7340
print("seconds is",seconds)
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print( hour,"hours",minutes,"minutes",seconds,"seconds")

