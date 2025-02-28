class Vector2D:
    def __init__(self, *v):
        if len(v) == 0: # нульовий вектор
            self.v1 = 0
            self.v2 = 0
            
        elif len(v) == 1: # тут будемо вважати, що
            if isinstance(v[0], Vector2D):
                self.v1, self.v2 = v[0].v1, v[0].v2
            else:
                self.v1, self.v2 = v[0]
        elif len(v) == 2: # два числа
            self.v1, self.v2 = v
        else: # 4, 5, 6
            raise ValueError("По таких даних неможливо створити вектор!")

    def __str__(self):
        return f"{self.v1:3.2f}, {self.v2:3.2f}"


if __name__ == '__main__':
    v = Vector2D(1, 2)
    print(v)
