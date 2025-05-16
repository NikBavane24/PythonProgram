from abc import abstractmethod, ABC


class Oops:

    def __init__(self):
        print("Constructor")

    def method(self):
        print("Method")

o1=Oops()
o1.method()

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")
a1=Cat()
a1.sound()
a2=Dog()
a2.sound()
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
d = Dog()

a.speak()  # Animal speaks
d.speak()  # Dog barks
class Person:
    def __init__(self, name,age):
        self.name = name        # Public
        self.age = age
        self._address = "Hidden"  # Protected (convention)
        self.__salary = 5000    # Private

    def display_info(self):
        print(f"Name: {self.name},Age:{self.age}, Salary: {self.__salary}")
p = Person("Alice", 30)
print(p.name)           # ✅ Public: OK
print(p.age)            # ✅ Public: OK
print(p._address)       # ⚠️ Protected: Possible, but discouraged
#print(p.__salary)     # ❌ Error: private attribute
print(p._Person__salary)  # ✅ Works using name mangling
