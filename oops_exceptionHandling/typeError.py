#python program that prompts the user to input 2 numbers and raises a
#typerror expection if the inputs are not numerical


def get_numeric_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num  # Return the numeric input if successful
        except ValueError:
            print("Error: Please enter a valid number.")

try:
    # Get first number from user
    num1 = get_numeric_input("Enter the first number: ")
    
    # Get second number from user
    num2 = get_numeric_input("Enter the second number: ")

    # Print the sum of the two numbers
    print(f"The sum of {num1} and {num2} is: {num1 + num2}")

except TypeError as e:
    print(f"TypeError: {e}")
