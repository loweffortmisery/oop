from Circle import Circle
from Triangle import Triangle
from Rectangle import Rectangle
from Trapeze import Trapeze
from Parallelogram import Parallelogram
from Ball import Ball
from TriangularPyramid import TriangularPyramid
from QuadrangularPyramid import QuadrangularPyramid
from RectangularParallelepiped import RectangularParallelepiped
from Cone import Cone
from TriangularPrism import TriangularPrism



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
                elif name == "Ball" and len(params) == 1:
                    shapes.append(Ball(*params))
                elif name == "TriangularPyramid" and len(params) == 2:
                    shapes.append(TriangularPyramid(*params))
                elif name == "QuadrangularPyramid" and len(params) == 3:
                    shapes.append(QuadrangularPyramid(*params))
                elif name == "RectangularParallelepiped" and len(params) == 3:
                    shapes.append(RectangularParallelepiped(*params))
                elif name == "Cone" and len(params) == 2:
                    shapes.append(Cone(*params))
                elif name == "TriangularPrism" and len(params) == 4:
                    shapes.append(TriangularPrism(*params))
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
        max_volume = [None, None]
        for shape in shapes:
            if max_volume[1] == None or max_volume[1] < shape.volume():
                max_volume = [shape, shape.volume()]
        print(f"Фігура з найбільшою мірою це: {max_volume[0]}\nМіра = {max_volume[1]}")

