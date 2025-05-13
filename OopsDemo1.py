#self keyword is mandatory to call variable into the method
# instance and class variable have whole different purpose.
# constructor name should be __init__
# new keyword not required when you create object

class A:
    a=100               #class variable
    def method(self):
        print("Oops Concept in Python")

    def __init__(self):
        print("I am called automatically when constructor is created")

#o =A()                  #syntax to create an object
#o.method()
#print(o.a)