

class Shape:
    def __init__(self,colour,is_filled):
        self.colour =colour
        self.is_filled = is_filled


class Circle(Shape):
    def __init__(self,colour,is_filled,radius):
        super().__init__(colour,is_filled)
        self.radius=radius
        
        
class Square(Shape):
    def __init__(self, colour, is_filled, side):
        super().__init__(colour, is_filled)
        self.side = side
        
        
        
class Triangle(Shape):
    def __init__(self, colour, is_filled, width,height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height


Circle = Circle(colour="red",is_filled=True,radius=10)

print(Circle.colour,Circle.radius,Circle.is_filled)
