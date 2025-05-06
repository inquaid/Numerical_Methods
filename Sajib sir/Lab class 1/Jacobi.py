import re

def f1(x2, x3):
    return (d1 - (b1 * x2) - (c1 * x3)) / a1

def f2(x1, x3):
    return (d2 - (a2 * x1) - (c2 * x3)) / b2

def f3(x1, x2):
    return (d3 - (a3 * x1) - (b3 * x2)) / c3



n = int(input("Degree: "))

equation = input("Equation: ")

coefficients = {}

terms = re.findall(r'([+-]?\d*)x\^?(\d*)|([+-]?\d+)', equation.replace(" ", ""))

# print(terms)
# term[0] = coefficient
# term[1] = exponent
# term[2] = constant

for term in terms:
    if term[0]: 
        coefficient = term[0]
        power = term[1] if term[1] else '1'  
        coefficient = int(coefficient) if coefficient not in ['+', '-'] else int(coefficient + '1')
        coefficients[int(power)] = coefficient
    elif term[2]:  
        coefficients[0] = int(term[2])

for i in range(n, -1, -1):
    coefficient = coefficients.get(i, 0)  
    print(f"Coefficient of x^{i}: {coefficient}")


x1 = 0.0
x2 = 0.0
x3 = 0.0

i = 0

a1 = int(input("eqn1 a: "))
b1 = int(input("eqn1 b: "))
c1 = int(input("eqn1 c: "))
d1 = int(input("eqn1 d: "))

a2 = int(input("eqn2 a: "))
b2 = int(input("eqn2 b: "))
c2 = int(input("eqn2 c: "))
d2 = int(input("eqn2 d: "))

a3 = int(input("eqn3 a: "))
b3 = int(input("eqn3 b: "))
c3 = int(input("eqn3 c: "))
d3 = int(input("eqn3 d: "))

prevx1 = x1
prevx2 = x2
prevx3 = x3
while i < 1700:
    print(f"{x1}, {x2}, {x3}")

    temp = f1(x2, x3)
    temp2 = f2(x1, x3)
    x3 = f3(x1, x2)
    x1 = temp
    x2 = temp2
    
    # if(x1 ==prevx1 and x2 == prevx2 and x3 == prevx3 ):
    #     break

    i += 1