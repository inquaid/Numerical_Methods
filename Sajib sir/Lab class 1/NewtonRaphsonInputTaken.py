import Equation_Parser as ep
def func(x):
    # x^2 - 3x + 2
    a = 1
    b = -3
    c = 2
    return (a * x * x) + (b * x) + c

def ddx_func(x):
    # 2x - 3
    # a = 0
    d = 2
    e = -3
    return (d*x) + e

i = 0
x1 = 0  

eqn = input("Equation: ")
prsr = ep.EquationParser(eqn)
prsr.parsePolynomial()
a, b, c = prsr.get_coefficients(2, 1, 0)
d, e = prsr.derivative()
# print(prsr.derivative())

while i < 10:
    print(x1)
    x2 = x1 - (func(x1) / ddx_func(x1))
    x1 = x2
    i+=1
    
# print(x1)