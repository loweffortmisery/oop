from Figure import Figure
from Rectangle import Rectangle
from Triangle import Triangle
class QuadrangularPyramid(Rectangle):
    def __init__(self, a,b,height):
        assert (a > 0 and b > 0 and height > 0), "Неможливо утворити фігуру з такими сторонами"
        self.__dimention = 3
        self.base_edge1 = a
        self.base_edge2 = b
        self.base = Rectangle(a,b)
        self.edge = ((((a**2 + b**2)**0.5)/2)**2 + height**2)**0.5
        self.side1 = Triangle(a,self.edge,self.edge)
        self.side2 = Triangle(b,self.edge,self.edge)
        self.__height = height
  
    @property
    def dimention(self):
        return self.__dimention

    @property
    def height(self):
        return self.__height

   
    def squareBase(self):
        return self.base.square()

    def squareSurface(self):
        return [self.side1.square(), self.side2.square()]
    def volume(self):
        return (1/3)*self.squareBase()*self.height

    def __str__(self):
        return f"QuadrangularPyramid: {self.base_edge1} {self.base_edge2} {self.height}"
