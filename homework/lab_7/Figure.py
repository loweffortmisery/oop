class Figure():
    def __init__(self, d):
        self.__dimention = d
    
    @property
    def dimention(self):
        return self.__dimention

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None
    @property
    def height(self):
        if(self.dimention == 3):
            return self.__height
        return None

    def volume(self):
        pass
