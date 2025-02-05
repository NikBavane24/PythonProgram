
#Syntax- def --init__(self):
#    Constructor body

class Class1:
    def __init__(self,a,b):
        print("Class1")
        self.a=a
        self.b=b

    def add(self):
        print(self.a + self.b)


c1=Class1(20,30)
c1.add()

c2=Class1(200,300)
c2.add()

class Constructor:
    def __init__(self):
        print("Constructor run")

c3=Constructor()