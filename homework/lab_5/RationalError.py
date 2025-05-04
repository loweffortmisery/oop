class RationalError(ZeroDivisionError):
    def __init__(self, message = "Знаменник не може дорівнювати нулю"):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"

class RationalValueError(ValueError):
    def __init__(self, message = "Дані не задають раціональне число"):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"

