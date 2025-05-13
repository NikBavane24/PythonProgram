class Shape:
    def area(self):
        print("Area of shape")

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area of Circle",3.14*self.radius*self.radius)

class square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print("Area of square=",self.side*self.side)
o1=Circle(10)
o2=square(5)

o1.area()
o2.area()
