from Figure import Figure

class Ball(Figure):
    def __init__(self, radius):
        assert (radius > 0), "Неможливо утворити фігуру з такими сторонами"
        super().__init__(3)
        self.radius = radius

    def volume(self):
        pi = 3.14
        return (4/3)*pi*(self.radius**3) 
    @property
    def height(self):
        return None
    def __str__(self):
        return f"Ball: {self.radius}"
