class Rectangle:
    def __init__(self, a, b):
        assert (a > 0 and b > 0), "Неможливо утворити прямокутник з такими сторонами"
        self.a = a
        self.b = b
    

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle: {self.a} {self.b}"
