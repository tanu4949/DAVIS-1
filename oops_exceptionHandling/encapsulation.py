#python program for encapsulation


class Car:
    def __init__(self, brand, model):
        self.brand = brand           # Public attribute
        self._model = model          # Protected attribute
        self.__mileage = 0          # Private attribute

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self._model}, Mileage: {self.__mileage}")

    def update_mileage(self, mileage):
        self.__mileage = mileage

# Creating an object of Car class
my_car = Car("Toyota", "Camry")

# Accessing public attribute directly
print(f"Brand: {my_car.brand}")

# Accessing protected attribute directly (not recommended but possible)
print(f"Model: {my_car._model}")

# Attempting to access private attribute directly will result in an AttributeError
# print(f"Mileage: {my_car.__mileage}")  # This will raise an AttributeError

# Instead, accessing private attribute using a getter method
print(f"Mileage: {my_car._Car__mileage}")  # Name mangling is used for private attributes

# Updating private attribute using a method
my_car.update_mileage(50000)

# Displaying car information
my_car.display_info()
