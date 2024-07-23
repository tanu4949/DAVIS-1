#python program for valueError exception

while True:
    try:
        num = int(input("Please enter a number: "))
        print("You entered:", num)
        break
    # Break out of the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
