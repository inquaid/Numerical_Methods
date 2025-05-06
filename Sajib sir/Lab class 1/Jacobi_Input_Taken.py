# import re

import Equation_Parser as ep


def f1(x2, x3):
    return (d1 - (b1 * x2) - (c1 * x3)) / a1


def f2(x1, x3):
    return (d2 - (a2 * x1) - (c2 * x3)) / b2


def f3(x1, x2):
    return (d3 - (a3 * x1) - (b3 * x2)) / c3


x1 = 0.0
x2 = 0.0
x3 = 0.0

i = 0

# equation1 = input("Equation: ")
equation1 = "4x-1y-1z=5"
prsr = ep.EquationParser(equation1)
prsr.parseSimul()
a1, b1, c1, d1 = prsr.get_coefficients("x", "y", "z", "constant")

# equation1 = input("Equation: ")
equation1 = "-1x+3y-1z=6"
prsr = ep.EquationParser(equation1)
prsr.parseSimul()
a2, b2, c2, d2 = prsr.get_coefficients("x", "y", "z", "constant")

# equation1 = input("Equation: ")
equation1 = "-1x-1y+5z=-4"
prsr = ep.EquationParser(equation1)
prsr.parseSimul()
a3, b3, c3, d3 = prsr.get_coefficients("x", "y", "z", "constant")

print(f"{a1} {b1} {c1} {d1}")
print(f"{a2} {b2} {c2} {d2}")
print(f"{a3} {b3} {c3} {d3}")

prevx1 = x1
prevx2 = x2
prevx3 = x3
while i < 50:
    # print(f"{x1}, {x2}, {x3}")

    temp = f1(x2, x3)
    temp2 = f2(x1, x3)
    x3 = f3(x1, x2)
    x1 = temp
    x2 = temp2

    # if(x1 ==prevx1 and x2 == prevx2 and x3 == prevx3 ):
    #     break

    i += 1

print(f"{x1} {x2} {x3}")
