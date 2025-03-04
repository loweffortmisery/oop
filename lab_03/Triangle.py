class Triangle:
    def __init__(self, a, b, c):
        assert (a + b > c and a + c > b and b + c > a), "Неможливо утворити трикутник з такими сторонами"
        self.a = a
        self.b = b
        self.c = c
    
    def Perimeter(self):
        return self.a + self.b + self.c




