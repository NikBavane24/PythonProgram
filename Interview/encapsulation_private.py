
class Car:
    def __init__(self):
        self.__price = 20000  # Private attribute

    def __show_price(self):  # Private method
        print(f"Price: {self.__price}")

    def public_method(self):
        # Accessing private method internally
        self.__show_price()

car = Car()
# print(car.__price)          # ❌ Error
# car.__show_price()          # ❌ Error
car.public_method()           # ✅ Works

# But can be accessed with name mangling (not recommended)
print(car._Car__price)        # ✅ Works but bad practice
