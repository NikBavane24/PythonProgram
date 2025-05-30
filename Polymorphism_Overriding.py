
class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
        print("Constructor of Parent class")
        #print("Inside Parent")

    # Parent's show method
    def show(self):
        print(self.value)

    # Defining child class
class Child(Parent):
    # Constructor
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.value = "Inside Child"
        print("Constructor of child class")
        #print("Inside Child")

    # Child's show method
    def show(self):
        #super().show()
        print(self.value)

    # Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()  # Should print "Inside Parent"
obj2.show()  # Should print "Inside Child"