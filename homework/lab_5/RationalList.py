from Rational import Rational

from RationalError import RationalError, RationalValueError

class RationalList_iterator:
    def __init__(self, collection: list):
        self.__collection = self.__custom_sort(collection)
        self.__current = 0
    @staticmethod
    def __custom_sort(rat_list):
        result = list(rat_list)
        _sorted = False
        while not _sorted:
            _sorted = True
            for i in range(1, len(result)):
                rat_1 = result[i-1]
                rat_2 = result[i]
                if ((rat_1.d < rat_2.d) or 
                    (rat_1.d == rat_2.d and rat_1.n < rat_2.n)):
                        result[i-1] = rat_2
                        result[i] = rat_1
                        _sorted = False
        return result

    def __next__(self):
        try:
            val = self.__collection[self.__current]
            self.__current += 1
            return val
        except IndexError:
            raise StopIteration

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
                        except RationalValueError as e:
                            raise e
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
            raise RationalValueError()
    
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
    
    def __iter__(self):
        return RationalList_iterator(self.__collection)


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
                except (RationalError, RationalValueError) as e:
                    raise e
                print(sum(rat_list), "\n", file = out)



def disp_iterated(filename,out):
    with open(out, 'a') as out:
        print("\n\n",filename, " :\n", file = out)
        with open(filename, 'r') as f:
            for line in f:
                els = line.strip().split()
                if not els:
                    continue
                try:
                    rat_list = RationalList(*els)
                except (RationalError, RationalValueError) as e:
                    raise e
                print(*rat_list, "\n", file = out)



if __name__ == '__main__':
    rl = RationalList([3,4,"ss"])
    filenames = ['RationalList_input/input01.txt', 'RationalList_input/input02.txt', 'RationalList_input/input03.txt']
   # for filename in filenames:
   #     find_sums(filename,'RationalList_out.txt')
    for filename in filenames:
        disp_iterated(filename,'RationalList_iterator_out.txt')



