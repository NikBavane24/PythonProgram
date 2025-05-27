class Car:
    def __init__(self):
        self.brand = "Toyota"  # Public attribute

    def show(self):
        print(f"Brand: {self.brand}")  # Public method


car = Car()
car.show()  # OK
print(car.brand)  # OK
