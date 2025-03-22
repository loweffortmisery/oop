from Figure import Figure
from Rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
    def __init__(self, a,b,c):
        assert(a > 0 and b > 0 and c > 0), "Неможливо утворити фігуру з такими сторонами"
        self.__dimention = 3 
        self.base_edge1 = a
        self.base_edge2 = b
        self.__height = c
        self.base = Rectangle(self.base_edge1, self.base_edge2)
        self.side1 = Rectangle(self.base_edge1, self.__height)
        self.side2 = Rectangle(self.base_edge2, self.__height)
 
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
        return self.squareBase() * self.height
    
        
