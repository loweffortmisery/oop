from Figure import Figure
from Circle import Circle

class Cone(Circle):
    def __init__(self, radius, height):
        assert(radius > 0, height > 0),"Неможливо утворити фігуру з такими сторонами"
        self.__dimention = 3
        self.__height = height
        self.base_radius = radius 
        self.base = Circle(self.base_radius)
    
    @property
    def dimention(self):
        return self.__dimention

    @property
    def height(self):
        return self.__height

    def squareBase(self):
        return self.base.square()

    def squareSurface(self):
        pi = 3.14
        return pi*self.base_radius*(self.base_radius**2 + self.height**2)**0.5

    def volume(self):
        return (1/3)*self.squareBase()*self.height

    def __str__(self):
        return f"Cone: {self.base_radius} {self.height}"
