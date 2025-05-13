import self

class Variables:

    b=20

    def local_variable(self):
        a=10
        print(a)
        print(Variables.b)
    print("---------------------------------------------")
    def global_variable(self):
        print(Variables.b)
        Variables.b=50
        print(Variables.b)

c1=Variables
c1.local_variable(self)
c1.global_variable(self)