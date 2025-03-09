from Circle import Circle
from Triangle import Triangle
from Rectangle import Rectangle
from Trapeze import Trapeze
from Parallelogram import Parallelogram




def read(filename):
    shapes = []
    with open(filename, "r") as f:
        for line in f:
            data = line.split()
            if not data:
                continue
            name = data[0]
            params = [float(el) for el  in data[1:]]
            try:
                if name == "Triangle" and len(params) == 3:
                    shapes.append(Triangle(*params))
                elif name == "Rectangle" and len(params) == 2:
                    shapes.append(Rectangle(*params))
                elif name == "Trapeze" and len(params) == 4:
                    shapes.append(Trapeze(*params))
                elif name == "Parallelogram" and len(params) == 3:
                    shapes.append(Parallelogram(*params))
                elif name == "Circle" and len(params) == 1:
                    shapes.append(Circle(*params))
            except AssertionError:
                continue;
    return shapes

if __name__ == "__main__":
    filenames = ["input01.txt", "input02.txt", "input03.txt"]
    for filename in filenames:
        shapes = read(filename)
        if len(shapes) == 0:
            print("У файлі немає коректних фігур")
            continue
        max_perimeter = [0, None]
        max_area = [0, None]
        for shape in shapes:
            if isinstance(shape.area(), complex):
                print(shape)
                continue
            if shape.perimeter() > max_perimeter[0]:
                max_perimeter = [shape.perimeter(), shape]
            if shape.area() > max_area[0]:
                max_area = [shape.area(), shape]
        print(f"Фігура з найбільшою площею це: {max_area[1]}\nПлоща = {max_area[0]}")
        print(f"Фігура з найбільшим периметром це: {max_perimeter[1]}\nПериметр = {max_perimeter[0]}")
