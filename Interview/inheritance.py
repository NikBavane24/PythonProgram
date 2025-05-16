import self


class Parent:
    def speak(self):
        print("I am the parent.")

class Child(Parent):
    def greet(self):
        print("Hello, I am the child.")
o1=Child
o1.speak(self)
o1.greet(self)