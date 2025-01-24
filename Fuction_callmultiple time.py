

class MyClass:
    def __init__(self):
        print("Constructor")
    def my_fun(self):
        print("Hello")

m1=MyClass()
m2=MyClass()

for i in range(5):
    m1.my_fun()