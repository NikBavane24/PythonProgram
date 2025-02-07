

class method_overloading:
    def method1(self):
        print("method1")

    def method1(self,a):
        self.a=a
        print("method1 with parameter")

    def method1(self,a,b):
        self.a=a
        self.b=b
        print("method1 with 2 parameter")

c1=method_overloading()
c1.method1(1,"N")