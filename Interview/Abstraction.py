from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Dog sound = Bark")

class Cat(Animal):
    def make_sound(self):
        print("Cat sound = Meow")
d = Dog()
d.make_sound()  # Output: Bark

c = Cat()
c.make_sound()  # Output: Meow
