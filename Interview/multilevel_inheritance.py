class Grandparent:
    def say_hello(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def say_hi(self):
        print("Hi from Parent")

class Child(Parent):
    def say_hey(self):
        print("Hey from Child")

c = Child()
c.say_hello()  # Inherited from Grandparent
c.say_hi()     # Inherited from Parent
c.say_hey()    # From Child
