import math


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        pi = math.pi
        print(pi * self.r * self.r)


c1 = Circle(10)
c1.area()