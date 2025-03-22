from Figure import Figure

class Parallelogram(Figure):
    def __init__(self, side1, side2, height):
        assert(side1 > 0 and side2 > 0 and  height > 0), "Неможливо утворити паралелограм з такими сторонами"
        super().__init__(2)
        self.side1 = side1
        self.side2 = side2
        self.__height = height
    
    def perimeter(self):
        return (self.side1 + self.side2)*2
    
    def square(self):
        return self.side2 * self.__height        
    def volume(self):
        return self.square()
    def __str__(self):
        return f"Parallelogram: {self.side1} {self.side2} {self.__height}" 
