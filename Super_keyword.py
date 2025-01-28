import Super_keyword


class Parent():
    def Parent1(self):
        print("Parent class implementation")

class Child(Parent):
    def Parent1(self):
        print("Parent method implementation from child class")

    def child1(self):
        print("Child method implementation from child class")
        Super_keyword.Parent

o1=Child()
o2=Parent()
o1.Parent1()
o1.child1()
o2.Parent1()





