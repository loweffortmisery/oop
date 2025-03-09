class Triangle: 
    def __init__(self, a, b, c):
        assert (a + b > c and a + c > b and b + c > a), "Неможливо утворити трикутник з такими сторонами"
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"Triangle: {self.__position, self.__vertex1, self.__vertex2}"
 
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = (self.a + self.b + self.c)/2
        p_a = p - self.a
        p_b = p - self.b
        p_c = p - self.c
        return (p * p_a * p_b * p_c)**0.5







