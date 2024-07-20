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
