class Parallelogram:
    def __init__(self, side1, side2, height):
        assert(side1 > 0 and side2 > 0 and  height > 0), "Неможливо утворити паралелограм з такими сторонами"
        self.side1 = side1
        self.side2 = side2
        self.height = height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.height
    
    def area(self):
        return self.side2 * self.height        

    def __str__(self):
        return f"Parallelogram: {self.side1} {self.side2} {self.height}" 
