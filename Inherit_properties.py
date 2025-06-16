import self


class addition:
    def __init__(self):
        print("Constructor of addition class")
    def add(self,a,b):
        self.a=a
        self.b=b
        sum=a+b
        print(sum)


class execution(addition):
    def __init__(self):
        super().__init__()
        print("Constructor of execution class")
    def add1(self):
        print("Execution class")

o2=execution()

o2.add(100,50)
o2.add1()




