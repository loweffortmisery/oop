from Figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        assert (a > 0 and b > 0), "Неможливо утворити фігуру з такими сторонами"
        super().__init__(2)
        self.a = a
        self.b = b
    

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b
    
    def volume(self):
        return self.square()
    
    def __str__(self):
        return f"Rectangle: {self.a} {self.b}"
