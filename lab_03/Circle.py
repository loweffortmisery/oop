class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        pi = 3.14
        return 2*(pi)*self.radius

    def area(self):
        pi = 3.14
        return pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle: {self.radius}"
