

class MyClass:
    def __init__(self):
        print("Constructor")
    def my_fun(self):
        print("Method")

m1=MyClass()
m2=MyClass()
m2.my_fun()

for i in range(5):
    print(i)
    m1.my_fun()

def Method1():
    print("Method1")

Method1()