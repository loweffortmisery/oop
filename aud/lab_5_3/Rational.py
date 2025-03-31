class Rational():
    def __init__(self, *args):
        if len(args) == 2 and type(args[0]) == int and type(args[1]) == int and args[1] != 0:
            self.n = n
            self.d = d
            if self.n == 0:
                self.sign = 0
            else:
                self.sign = -1 if self.n/self.d < 0 else 1
        elif len(args) == 1:
            if isinstance(args[0], Rational):
                self.n = args[0].n
                self.d = args[0].d
                self.sign = args[0].sign
            elif isinstance(args[0], str):
                s = args[0].strip()
                try:
                    self.n, self.d = (int(el) for el in s.split('/'))
                    if self.d == 0:
                        raise ValueError
                    if self.n == 0:
                        self.sign = 0
                    else:
                        self.sign = -1 if self.n/self.d < 0 else 1
       
                except ValueError:
                    raise ValueError("Некоректні дані")
            else:
                raise ValueError("Некоректні дані")
        else:
            raise ValueError("Некоректні дані")
        
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

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.n + other.n, self.d + other.d)
        elif isinstance(other, Ra)



    def __str__(self):
        return f"{self.n}/{'(' if self.d < 0}{self.d}{')' if self d < 0}"

    
