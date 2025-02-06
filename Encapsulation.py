


class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute


class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()