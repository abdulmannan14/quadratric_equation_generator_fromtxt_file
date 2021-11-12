import cmath
from math import *


def quadratic_calculator(value_of_a, value_of_b, value_of_c):
    a = float(value_of_a)
    b = float(value_of_b)
    c = float(value_of_c)
    print(f"We have a 'A' value of {a}")
    print(f"We have a 'B' value of {b}")
    print(f"We have a 'C' value of {c}")
    # calculate the discriminant
    bsquareminus4ac = (b ** 2) - (4 * a * c)
    print(f"We have a bsquaredminus4ac value of {bsquareminus4ac}")
    if bsquareminus4ac > 0:
        # find two solutions
        sol1 = (-b - cmath.sqrt(bsquareminus4ac)) / (2 * a)
        sol2 = (-b + cmath.sqrt(bsquareminus4ac)) / (2 * a)
        sol1 = round(sol1.real, 2) + round(sol1.imag, 2) * 1j
        sol2 = round(sol2.real, 2) + round(sol2.imag, 2) * 1j
        sol1 = complex(sol1, 0).real
        sol2 = complex(sol2, 0).real


        print('The solution are {0} and {1}'.format(sol1, sol2))
        print("================================================")
    elif bsquareminus4ac == 0:
        pass
    else:
        print("No Solution")
        print("================================================")


def TheGistOfLine(astring):
    # typical astring would be like  "4,(1,2),(23.4,10) "
    splitted_string = astring.split(",")
    return (splitted_string)


def ShowSolution(ProblemLine):
    # define constants to access ProblemLine in a more English like way
    value_of_a = ProblemLine[1]
    value_of_b = ProblemLine[2]
    value_of_c = ProblemLine[3]
    get_quadratic_calculation = quadratic_calculator(value_of_a, value_of_b, value_of_c)


Done = False;
DFile = open("data.txt", "r")
ProblemLine = []
iterator = 1
while (not Done):
    astring = DFile.readline()

    if (astring.strip() == "zz"):
        Done = True
        print("The program has been completed")
    else:
        print(f"doing problem no. {iterator} from  data.txt file")
        ProblemLine = TheGistOfLine(astring)
        ShowSolution(ProblemLine)
    iterator = iterator + 1
