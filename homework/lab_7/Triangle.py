from Figure import Figure

class Triangle(Figure): 
    def __init__(self, a, b, c):
        super().__init__(2)
        assert (a + b > c and a + c > b and b + c > a), "Неможливо утворити трикутник з такими сторонами"
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"Triangle: {self.a, self.b, self.c}"
 
    def perimeter(self):
        return self.a + self.b + self.c
    
    def square(self):
        p = (self.a + self.b + self.c)/2
        p_a = p - self.a
        p_b = p - self.b
        p_c = p - self.c
        return (p * p_a * p_b * p_c)**0.5
   
    def volume(self):
        return self.square()






