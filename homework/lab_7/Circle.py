from Figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        assert (radius > 0), "Неможливо утворити фігуру з такими сторонами"
        super().__init__(2)
        self.radius = radius

    def perimeter(self):
        pi = 3.14
        return 2*(pi)*self.radius

    def square(self):
        pi = 3.14
        return pi * (self.radius ** 2)
    def volume(self):
        return self.square()
    def __str__(self):
        return f"Circle: {self.radius}"
