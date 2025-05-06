import re

n = int(input("Degree: "))

equation = input("Equation: ")

coefficients = {}

terms = re.findall(r'([+-]?\d*)x\^?(\d*)|([+-]?\d+)', equation.replace(" ", ""))


print(terms)
# print(equation.replace(" ", ""))
# print(equation)
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

print(coefficients)
for i in range(n, -1, -1):
    coefficient = coefficients.get(i, 0)  
    print(f"Coefficient of x^{i}: {coefficient}")
