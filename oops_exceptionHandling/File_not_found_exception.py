#python program for FileNotFound exception handling

while True:
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
        break  # Exit the loop if file is successfully opened and read
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please enter a valid filename.")
    except IOError as e:
        print(f"Error: Unable to open file '{filename}'. Error message: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
