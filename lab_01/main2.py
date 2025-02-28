from QuadraticEquation import QuadraticEquation


def print_eqs(name, eqs):
    print(name)
    for eq in eqs:
        eq.show()

if __name__ == '__main__':
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    for file in input_files:
        no_solutions = []
        one_solution = []
        max_solution = None
        equation_with_max_solution = None
        
        min_solution = None
        equation_with_min_solution = None

        two_solutions = []
        infinite_solutions = []
        with open(file, "r") as f:
            for line in f:
                try:
                    #print(line.split())
                    a, b, c = [int(el) for el in line.split()]
                except ValueError:
                    continue
                eq = QuadraticEquation(a, b, c)
                number_of_solutions = eq.solutions_number()
                if number_of_solutions == -1:
                    infinite_solutions.append(eq)
                elif number_of_solutions == 0:
                    no_solutions.append(eq)
                elif number_of_solutions == 1:
                    one_solution.append(eq)
                else:
                    two_solutions.append(eq)
                
                if number_of_solutions == 1:
                    solution = eq.solve()[0]
                    if max_solution == None:
                        max_solution = min_solution = solution
                        equation_with_min_solution = eq
                        equation_with_max_solution = eq
                    elif max_solution < solution:
                        max_solution = solution
                        equation_with_min_solution = eq
                    elif min_solution > solution:
                        min_solution = solution
                        equation_with_min_solution = eq
                    else:
                        pass
        print_eqs("Рівняння, що не мають розв'язків:", no_solutions)
       
        print_eqs("Рівняння, що мають 1 розв'язок:", one_solution)
        
        print_eqs("Рівняння, що мають 2 розв'язки:", two_solutions)
        
        print_eqs("Рівняння, що мають безліч розв'язків:", infinite_solutions)
        print("Рівняння, що має мінімальний розв'язок, серед тих що мають 1 розв'язок:")
        equation_with_min_solution.show()

        print("Рівняння, що має максимальний розв'язок, серед тих що мають 1 розв'язок:")
        equation_with_max_solution.show()
