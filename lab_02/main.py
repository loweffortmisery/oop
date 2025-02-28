from Vector2D import Vector2D
from Solver import Solver
from Matrix2D import Matrix2D
import sys

def solve(matrix_file, rhs_file, out_file = None):
    matrices = []
    rhs = []
    with open(matrix_file, "r") as f:
        for line in f:
            if len(line.split()) == 0:
                continue
            matrices.append(Matrix2D([int(el) for el in line.split()]))
    with open(rhs_file, "r") as f:
        for line in f:
            if len(line.split()) == 0:
                continue
            rhs.append(Vector2D([int(el) for el in line.split()]))
    if out_file is not None:
        out = open(out_file, 'w')
    else:
        out = sys.stdout

    for i in range(len(matrices)):
        s = Solver(matrices[i], rhs[i])
        x = s.solve()
        print(x, file=out)

    if out_file is not None:
        out.close()    


if __name__ == "__main__":
    solve("matrix_coefficients.txt", "rhs_values.txt", "solutions_file.txt")
