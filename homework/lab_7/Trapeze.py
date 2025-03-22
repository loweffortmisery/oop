from Figure import Figure

class Trapeze(Figure):
    def __init__(self, base1, base2, side1, side2):
        assert (
            base1 > 0
            and base2 > 0
            and side1 > 0
            and side2 > 0
            and (
                (base1 == base2 and side1 == side2)
                or (
                    base1 != base2
                    and 4 * side1**2 * (abs(base1 - base2)) ** 2
                    >= ((abs(base1-base2))**2 + side1**2 - side2**2) ** 2
                    and 4 * side2**2 * (abs(base1-base2))**2
                    >= ((abs(base1-base2))**2 - side1**2 + side2**2) ** 2
                )
            )
        ), "Неможливо утворити трапецію з такими сторонами"
        super().__init__(2)
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def square(self):
        if self.base1 == self.base2:
            return self.base1 * self.side1
        base_diff = abs(self.base1 - self.base2)
        x = ((base_diff) ** 2 + self.side1 ** 2 - self.side2 ** 2)/(2*(base_diff)) 
        h = (self.side1 ** 2 - x ** 2) ** 0.5
        return (self.base1 + self.base2) * h

    def volume(self):
        return self.square()


    def __str__(self):
        return f"Trapeze: {self.base1} {self.base2} {self.side1} {self.side2}"
        
