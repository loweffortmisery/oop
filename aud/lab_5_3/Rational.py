




class Rational():
    def __init__(self, *args):
        if len(args) == 2 and type(args[0]) == int and type(args[1]) == int and args[1] != 0:
            self.n = args[0]
            self.d = args[1]
        elif len(args) == 1:
            if isinstance(args[0], Rational):
                self.n = args[0].n
                self.d = args[0].d
            elif isinstance(args[0], int):
                self.n = args[0]
                self.d = 1
            elif isinstance(args[0], str):
                s = args[0].strip().split('/')
                if len(s) == 1 or len(s) == 2:
                    try:
                        els = [int(el) for el in s]
                        rat = Rational(*els)
                        self.n = rat.n
                        self.d = rat.d
                        del rat
                    except ValueError:
                        raise ValueError("Некоректні дані")
                else:
                    raise ValueError("Некоректні дані")
            else:
                raise ValueError("Некоректні дані")
        else:
            raise ValueError("Некоректні дані")
        
        self.reduce()

    def __getitem__(self,key):
        if key == "n":
            return self.n
        if key == "d":
            return self.d
        raise KeyError

    def __setitem__(self,key,value):
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise ValueError("Не можна ділити на 0")
            self.d = value
        else:
            raise KeyError
    
    @staticmethod
    def __gcd(a,b):
        while b>0:
            a, b = b, a%b
        return a

    def reduce(self):
        if self.n == 0:
            return
        div = self.__gcd(abs(self.n),abs(self.d))
        self.n = self.n//div
        self.d = self.d//div
    
    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)
        elif isinstance(other, int):
            return Rational(self.n * other, self.d)
            
    def __rmul__(self,other):
        return self * other

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.n * other.d + other.n * self.d, self.d * other.d)
        elif isinstance(other, int):
            return Rational(self.n + other * self.d, self.d)
    def __radd__(self,other):
        return self + other

    def __sub__(self,other):
        return self + other * (-1)
    #    if isinstance(other, Rational):
    #        return Rational(self.n * other.d - other.n * self.d, self.d * other.d)
    #    elif isinstance(other, int):
    #        return Rational(self.n - other * self.d, self.d)
    #
    def __rsub__(self, other):
        return (-1)*self + other
    #    if isinstance(other, Rational):
    #        return Rational(-self.n * other.d + other.n * self.d, self.d * other.d)
    #    elif isinstance(other, int):
    #        return Rational(-self.n + other * self.d, self.d)
    #

    def __truediv__(self,other):
        divisor = Rational(other)
        if divisor.n == 0:
            raise ZeroDivisionError
        inv = Rational(divisor.d, divisor.n)
        return self * inv

    def __rtruediv__(self,other):
        if self.n == 0:
            raise ZeroDivisionError
        inv = Rational(self.d, self.n)
        return inv * other
    
    def __str__(self):
        return f"{self.n}/{'(' if self.d < 0 else ''}{self.d}{')' if self.d < 0 else ''}"

    def __repr__(self):
        return str(self)

def solve(filename):
    with open(filename, 'r') as f:
        for line in f:
            els = line.strip().split()
            if not els:
                continue
            try:
                Rationals = []
                operations = []
                i = 0
                while i < (len(els)):
#                    print(el)
                    if els[i] in {'+','-'}:
                        operations.append(els[i])
                    elif els[i] == '*':
                        Rationals[-1] *= Rational(els[i+1])
                        i += 1
                    elif els[i] == '/':
                        Rationals[-1] /= Rational(els[i+1])
                        i+=1
                    else:
                        Rationals.append(Rational(els[i]))
                    i += 1
            except (ValueError, ZeroDivisionError):
                raise ValueError("Некоректні дані")
#            print(Rationals)
#            print (operations)
            res = Rationals[0]
            i = 0
            for operation in operations:
                i+=1
                if operation == '+':
                    res += Rationals[i]
                elif operation == '-':
                    res -= Rationals[i]
                elif operation == '*':
                    res *= Rationals[i]
                elif operation == '/':
                    res /= Rationals[i]
                else:
                    raise AssertionError

            print(res)

if __name__ == '__main__':
    r1 = Rational(1,2)
    print(5 + r1)
    filenames = ['input01.txt']
    for filename in filenames:
        solve(filename)
