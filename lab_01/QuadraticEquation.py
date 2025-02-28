class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
#        self.d = self.b ** 2 - 4 * self.a * self.c

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")
    
    def discriminant(self):
        #if self.a == 0:
        #    return None
        return self.b ** 2 - 4 * self.a * self.c

    def solutions_number(self):
        solutions = self.solve()
        if len(solutions) == 1 and solutions[0] == "Нескінченна кількість розв'язків":
            #return "Нескінченна кількість розв'язків"
            return -1
        else:
            return len(solutions)

    def solve(self):         
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return ("Нескінченна кількість розв'язків", )
                return ()
            return (-self.c/self.b, )
   
        d = self.discriminant()
        if d < 0:
            return ()
        elif d == 0:
            return (-self.b/(2*self.a), )
        else:
            x1 = (-self.b + d**0.5)/(2*self.a)
            x2 = (-self.b - d**0.5)/(2*self.a)
            return (x1, x2)

if __name__ == '__main__':
    eq = QuadraticEquation(30, -92, 26)
    eq.show()
    print(eq)
