from Figure import Figure
from Triangle import Triangle

class TriangularPyramid(Triangle):
    def __init__(self, a, height):
        assert (a > 0 and height > 0), "Неможливо утворити фігуру з такими сторонами"
        self.base_edge = a
        self.base = Triangle(a,a,a)
        self.edge = (height**2 + (a**2)/3)**0.5
        self.side = Triangle(a,self.edge, self.edge)
        self.__dimention = 3
        self.__height = height
    def __str__(self):
        return f"TriangularPyramid: {self.base_edge} {self.height}"
 
    @property
    def dimention(self):
        return self.__dimention

    @property
    def height(self):
        return self.__height


    def squareSurface(self):
        return self.side.square()

    def squareBase(self):
        return self.base.square()
    def volume(self):
        return (self.squareBase()*self.height)/3
