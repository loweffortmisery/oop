from Rational import Rational
class RationalList:
    def __init__(self, *args):
        self.__collection = []
        if len(args) != 0:
            if len(args) == 1 and isinstance(args[0], RationalList):
                self.__collection += args[0].__collection
            else:
                items = []
                for arg in args:
                    if not isinstance(arg, Rational):
                        try:
#                            print(arg)
                            rat = Rational(arg)
                            items.append(rat)
                        except ValueError:
                            raise ValueError
                    else:
                        items.append(arg)
                self.__collection += items

    def __getitem__(self,key):
        return self.__collection[key]

    def __setitem__(self,key,value):
        if isinstance(value, Rational):
            self.__collection[key] = value
        elif isinstance(value, int) or isinstance(value, str):
            self.__collection[key] = Rational(value)
        else:
            raise TypeError("Це масив раціональних чисел")
    
    def __len__(self):
        return len(self.__collection)

    def __add__(self, other):
        result_list = []
        other_list = RationalList(other)
        for el in self.__collection:
            result_list.append(el)
        for el in other_list.__collection:
            result_list.append(el)
        return result_list


    def __radd__(self,other):
        result_list = []
        other_list = RationalList(other)
        for el in other_list.__collection:
            result_list.append(el)
        for el in self.__collection:
            result_list.append(el)
        return result_list


    def __iadd__(self,other):
        other_list = RationalList(other)
        self.__collection += other_list.__collection
    
    def __str__(self):
        return str(self.__collection)



def find_sums(filename,out):
    with open(out, 'a') as out:
        print("\n\n",filename, " :\n", file = out)
        with open(filename, 'r') as f:
            for line in f:
                els = line.strip().split()
                if not els:
                    continue
                try:
                    rat_list = RationalList(*els)
                except (ValueError, ZeroDivisionError):
                    raise ValueError("Некоректні дані")
                print(sum(rat_list), "\n", file = out)

if __name__ == '__main__':
    filenames = ['RationalList_input/input01.txt', 'RationalList_input/input02.txt', 'RationalList_input/input03.txt']
    for filename in filenames:
        find_sums(filename,'RationalList_out.txt')

