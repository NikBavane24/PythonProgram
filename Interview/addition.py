a=100
b=50

c=a+b
print("Addition=",c)

d=a-b
print("Subtraction=",d)

e=a*b
print("Multiplication=",e)

f=a/b
print('Division=',f)
print("------------------------------")
def method(a,b):
    g = a + b
    print("Addition=", g)

    h = a-b
    print("Subtraction=", h)

    i = a*b
    print("Multiplication=", i)

    j = a/b
    print('Division=', j)
method(200,100)
print("-----------------------------------------------")
class add:

    def __init__(self):
        print("Making an addition")

    def addition(self,a,b):
        c=a+b
        print("c=",c)

a=add()
a.addition(100,200)