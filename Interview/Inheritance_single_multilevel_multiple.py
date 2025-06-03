
class Parent:

    def name(self):
        print("Father")

class Child (Parent):

    def name(self):
        print("Son")

class Son (Child):

    def __init__(self):
        print("Contructor")

    def name(self):
        print("child")


c1=Child()
c1.name()
c2=Parent()
c2.name()
c3=Son()
c3.name()