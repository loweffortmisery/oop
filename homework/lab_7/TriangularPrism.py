from Figure import Figure
from Triangle import Triangle
from Rectangle import Rectangle
class TriangularPrism(Triangle):
    def __init__(self,a,b,c,h):
        assert(a > 0 and b > 0 and c > 0 and h > 0),"Неможливо утворити фігуру з такими сторонами"
        self.__dimension = 3
        self.__height = h
        self.base_edge1 = a
        self.base_edge2 = b
        self.base_edge3 = c
        self.base = Triangle(self.base_edge1, self.base_edge2, self.base_edge3)
        self.side1 = Rectangle(self.base_edge1, self.__height)
        self.side2 = Rectangle(self.base_edge2, self.__height)
        self.side3 = Rectangle(self.base_edge3, self.__height)
 
    @property
    def dimention(self):
        return self.__dimention

    @property
    def height(self):
        return self.__height


    def squareBase(self):
        return self.base.square()

    def squareSurface(self):
        return self.side1.square() + self.side2.square() + self.side3.square()

    def volume(self):
        return self.squareBase() * self.height

    def __str__(self):
        return f"TriangularPrism: {self.base_edge1} {self.base_edge2} {self.base_edge3} {self.height}"
