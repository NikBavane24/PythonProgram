class Car:
    def __init__(self):
        self._engine = "V8"  # Protected attribute

    def _start_engine(self):  # Protected method
        print("Engine started")


car = Car()
print(car._engine)  # Possible, but discouraged
car._start_engine()  # Possible, but discouraged
