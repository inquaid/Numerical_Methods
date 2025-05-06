import numpy as np
import re

class EquationParser:
    def __init__(self, equation):
        self.equation = equation.replace(" ", "")
        self.coefficients = {}
        
    def parsePolynomial(self):
        terms = re.findall(r'([+-]?\d*)x(\d+)', self.equation)
        # constant = re.search(r'=\s*([+-]?\d+)', self.equation)
        constant = re.search(r'([+-]?\d+\.?\d*)$', self.equation)
       
        for term in terms:
            coefficient = term[0]
            power = int(term[1])  
            
            if coefficient in ['', '+']:
                coefficient = 1
            elif coefficient == '-':
                coefficient = -1
            else:
                coefficient = int(coefficient)
            
            self.coefficients[power] = coefficient  
                
        # print(self.coefficients[3])
        # print(self.coefficients.get(3, 0))
        # print()
        if constant:
            self.coefficients[0] = int(constant.group(1))  
        else:
            self.coefficients[0] = 0  
                
    def parseSimul(self):
        
        terms = re.findall(r'([+-]?\d+)(\w+)', self.equation.split('=')[0])       
        
        constant = re.search(r'=\s*([+-]?\d+)', self.equation)
        
        for term in terms:
            coefficient = term[0]
            variable = term[1]
            
            coefficient = float(coefficient)  
            self.coefficients[variable] = coefficient  
            
        if constant:
            self.coefficients['constant'] = float(constant.group(1))  
        else:
            self.coefficients['constant'] = 0  
     
    def derivative(self):
        derivative_terms = []
        for power, coefficient in self.coefficients.items():
            if power > 0:  
                derivative_terms.append(coefficient * power)  
        return tuple(derivative_terms)

    def get_coefficients(self, *variables):
        
        return tuple(self.coefficients.get(var, 0) for var in variables)


def co_efficients(eqn):
    equation2 = eqn
    parser2 = EquationParser(equation2)
    parser2.parsePolynomial()  
    
    max_degree = max(parser2.coefficients.keys())
    
    coefficients = parser2.get_coefficients(*range(max_degree, -1, -1))
    
    return coefficients

# Example usage:
# eqn = "3x4-4x2 =-125"
# coefficients = co_efficients(eqn)
# print(f"Coefficients (from highest degree to constant): {coefficients}")
class Test:
    def __init__(self, eqn):
        self.symbol = "+"
        self.num = 0
        self.x = [-1, 1]  # x[0] = value, x[1] = power
        self.y = [-1, 1]  # y[0] = value, y[1] = power

        index = 0
        length = len(eqn)

        if eqn[0] == "-":
            self.symbol = "-"
            index += 1
        elif eqn[0] == "+":
            index += 1

        num_temp = ""
        while index < length and eqn[index].isdigit():
            num_temp += eqn[index]
            index += 1

        if num_temp:
            self.num = int(num_temp)
        elif index < length:
            self.num = 1

        while index < length and (eqn[index] == "x" or eqn[index] == "y"):
            if eqn[index] == "x":
                index += 1
                power_temp = ""
                while index < length and eqn[index].isdigit():
                    power_temp += eqn[index]
                    index += 1
                self.x[0] = 1
                if power_temp == "":
                    power_temp = "1"
                self.x[1] = int(power_temp)
            else:
                index += 1
                power_temp = ""
                while index < length and eqn[index].isdigit():
                    power_temp += eqn[index]
                    index += 1
                self.y[0] = 1
                if power_temp == "":
                    power_temp = "1"
                self.y[1] = int(power_temp)

    def calculate(self, x, y):
        if self.x[0] == -1:
            self.x[0] = 1
            self.x[1] = 1
        else:
            self.x[0] = x

        if self.y[0] == -1:
            self.y[0] = 1
            self.y[0] = 1
        else:
            self.y[0] = y
        val = self.num * (self.x[0] ** self.x[1]) * (self.y[0] ** self.y[1])
        if self.symbol == "-":
            return -val
        return val


def f(eqn="0", *args):
    x, y = (args + (0, 0))[:2]
    eqn = eqn.replace(" ", "")
    eqn = eqn.replace("+", " +")
    eqn = eqn.replace("-", " -")
    eqn = eqn.split(" ")
    res = 0
    for i in eqn:
        res += Test(i).calculate(x, y)
    return res


# if __name__ == "__main__":
#     eqn = "12x2y6+32x+5y"
#     eqn = eqn.replace(" ", "")
#     eqn = eqn.replace("+", " +")
#     eqn = eqn.replace("-", " -")
#     eqn = eqn.split(" ")

#     x = 2
#     y = 3
#     t = 0
#     for i in eqn:
#         t += Test(i).calculate(x, y)
#     print(t)

# import numpy as np
# import sys

# eqn, x1, x2 = "x2 - 4x - 10", 4, 2
# eqn = input()
# x1, x2 = list(map(int, (input().split())))

# x3 = 1000
# E = 0.001 
# while abs(x2-x1) > E:
#     f1 = f(eqn, x1)
#     f2 = f(eqn, x2)
#     x3 = ((f2 * x1) - (f1 * x2)) / (f2 - f1)
#     x1 = x2
#     x2 = x3
#     # print(x1, x2)
# print(x3)



# def f1(x2, x3):
#     return (d1 - (b1 * x2) - (c1 * x3)) / a1


# def f2(x1, x3):
#     return (d2 - (a2 * x1) - (c2 * x3)) / b2


# def f3(x1, x2):
#     return (d3 - (a3 * x1) - (b3 * x2)) / c3


# x1 = 0.0
# x2 = 0.0
# x3 = 0.0

# i = 0

# # equation1 = input("Equation: ")
# # equation1 = "4x-1y-1z=5"
# equation1 = input()
# prsr = EquationParser(equation1)
# prsr.parseSimul()
# a1, b1, c1, d1 = prsr.get_coefficients("x", "y", "z", "constant")

# # equation1 = input("Equation: ")
# # equation1 = "-1x+3y-1z=6"
# equation1 = input()
# prsr = EquationParser(equation1)
# prsr.parseSimul()
# a2, b2, c2, d2 = prsr.get_coefficients("x", "y", "z", "constant")

# # equation1 = input("Equation: ")
# # equation1 = "-1x-1y+5z=-4"
# equation1 = input()
# prsr = EquationParser(equation1)
# prsr.parseSimul()
# a3, b3, c3, d3 = prsr.get_coefficients("x", "y", "z", "constant")

# # print(f"{a1} {b1} {c1} {d1}")
# # print(f"{a2} {b2} {c2} {d2}")
# # print(f"{a3} {b3} {c3} {d3}")

# prevx1 = x1
# prevx2 = x2
# prevx3 = x3
# while i < 50:
#     # print(f"{x1}, {x2}, {x3}")

#     x1 = f1(x2, x3)
#     x2 = f2(x1, x3)
#     x3 = f3(x1, x2)

#     # if(x1 ==prevx1 and x2 == prevx2 and x3 == prevx3 ):
#     #     break

#     i += 1

# print(f"{x1} {x2} {x3}")


# import Equation_Parser as ep


# import Equation_Parser as ep


# def f(x):
#     return 3 * x * x + 1


# x0, y0, h = map(float, input().split())
# eqn = input()
# x0, y0, h, final = map(float, input().split())
# # print(f"{x0} {y0} {h}")

# print(f"xi = {x0} yi = {y0}")
# for _ in range(50):
#     y1 = y0 + (h * f(x0))
#     x0 = x0 + h
#     y0 = y1
#     print(f"xi = {x0} yi = {y1}")
#     if x0 == final:
#         break


#   Trapezoidal

# eqn = "0.2 + 25x - 200x2 + 675x3 - 900x4 + 400x5"
# eqn = input()
# # a = 0
# # b = 0.8
# # n = 2000
# a,b,n = list(map(int,input().split()))
# x1, x2 = list(map(int, (input().split())))

# step = (b - a) / n

# x_values = [a + i * step for i in range(n + 1)]

# print(f"f(1) = {f(eqn, 1)}")

# result = 0.5 * step * (
#     f(eqn, x_values[0]) + f(eqn, x_values[-1]) + 2 * sum(f(eqn, xi) for xi in x_values[1:-1])
# )

# print(f"Integral result using trapezoidal rule: {result}")

#   Simpson
# eqn = "0.2 + 25x - 200x2 + 675x3 - 900x4 + 400x5"
# eqn = input()
# # a = 0
# # b = 0.8
# # n = 10000  # Must be even for Simpson's 1/3 rule and a multiple of 3 for Simpson's 3/8 rule
# a,b,n = list(map(int,input().split()))

# # # Ensure `n` meets requirements for each rule
# # if n % 2 != 0:
# #     raise ValueError("n must be even for Simpson's 1/3 rule.")
# # if n % 3 != 0:
# #     raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule.")

# step = (b - a) / n
# x_values = [a + i * step for i in range(n + 1)]

# # Print f(x) for verification
# # print(f"f(1) = {f(eqn, 1)}")

# # Simpson's 1/3 Rule
# # simpson_1_3_result = (step / 3) * (
# #     f(eqn, x_values[0])
# #     + f(eqn, x_values[-1])
# #     + 4 * sum(f(eqn, x_values[i]) for i in range(1, n, 2))
# #     + 2 * sum(f(eqn, x_values[i]) for i in range(2, n, 2))
# # )

# # print(f"Integral result using Simpson's 1/3 rule: {simpson_1_3_result}")

# # # Simpson's 3/8 Rule
# simpson_3_8_result = (3 * step / 8) * (
#     f(eqn, x_values[0])
#     + f(eqn, x_values[-1])
#     + 3 * sum(f(eqn, x_values[i]) for i in range(1, n, 3))
#     + 3 * sum(f(eqn, x_values[i]) for i in range(2, n, 3))
#     + 2 * sum(f(eqn, x_values[i]) for i in range(3, n, 3))
# )

# print(f"Integral result using Simpson's 3/8 rule: {simpson_3_8_result}")


# from sympy import symbols, diff, sympify
# import re

# x = symbols("x")
# # eqn = "x2-3x+2"
# eqn = input()
# eqn = eqn.replace(" ", "")

# eqn = re.sub(r"(\d)(x)", r"\1*\2", eqn)
# eqn = re.sub(r"(x)(\d)", r"\1**\2", eqn)

# poly_expr = sympify(eqn)

# first_derivative = diff(poly_expr, x)

# _eqn = str(first_derivative).replace("*", "")
# eqn = eqn.replace("*", "")
# # print(eqn)
# # print(f(eqn, 0))
# x1 = 0
# x2 = 1000
# E = 0.00001
# # i = 0
# while True:
#     x2 = x1 - (f(eqn, x1) / f(_eqn, x1))
#     # i += 1
#     if abs(x2 - x1) < E:
#         break
#     x1 = x2
# print(x2)
# print(i)

# from sympy import symbols, lambdify, sympify

# x = symbols("x")
# x0 = 1.0  
# tol = 1e-6  
# max_iter = 100  

# # g_str = "x**2 + x - 2"  
# g_str = input()
# g = lambdify(x, sympify(g_str))

# xn = x0
# for i in range(max_iter):
#     xn_next = g(xn)  
    
#     if abs(xn_next - xn) < tol:
#         print(f"Root: {xn_next}, Iterations: {i + 1}")
#         break
    
#     xn = xn_next
# print(xn)
#Fitting Polynomial
# import numpy as np
# n = int(input())
# x = 0
# y = 0
# x2 = 0
# x3 = 0
# x4 = 0
# yx = 0
# yx2 = 0
# for _ in range(n):
#     Tx, Ty = list(map(float, input().split()))
#     # print(x, y)
#     x += Tx
#     y += Ty
#     x2 += (Tx ** 2)
#     x3 += (Tx ** 3)
#     x4 += (Tx ** 4)
#     yx += (Tx * Ty)
#     yx2 += (Ty * (Tx**2))
    
# print(f'The linear equation is: \n{n}a1 + {x}a2 + {x2}a3 = {y}')
# print(f'{x}a1 + {x2}a2 + {x3}a3 = {yx}')
# print(f'{x2}a1 + {x3}a2 + {x4}a3 = {yx2}')

# A = np.array([
#     [n, x, x2],
#     [x, x2, x3],
#     [x2, x3, x4]
# ])

# b = np.array([y, yx, yx2])

# # Solve the system of equations
# coefficients = np.linalg.solve(A, b)

# # Display the results
# print("\nThe coefficients of the polynomial are:")
# print(f"a1 (constant term) = {coefficients[0]}")
# print(f"a2 (linear term)   = {coefficients[1]}")
# print(f"a3 (quadratic term) = {coefficients[2]}")

# # Formulate the polynomial equation
# print("\nThe polynomial equation is:")
# print(f"y = {coefficients[0]} + {coefficients[1]}x + {coefficients[2]}x^2")
# def heun_method(eqn, x0, y0, x_end, h):
eqn = input()
x0, y0, x_end, h = list(map(float, input().split()))
x = x0
y = y0
result = [(x, y)]

# while x < x_end:
#     y_pred = y + h * f(eqn, x, y)  # Predictor (Euler's estimate)
#     y_corr = y + (h / 2) * (f(eqn, x, y) + f(eqn, x + h, y_pred))  # Corrector
#     x += h
#     y = y_corr
#     result.append((x, y))
# print(result)
# def runge_kutta_4th(eqn, x0, y0, x_end, h):
x = x0
y = y0
result = [(x, y)]

while x < x_end:
    k1 = h * f(eqn, x, y)
    k2 = h * f(eqn, x + h / 2, y + k1 / 2)
    k3 = h * f(eqn, x + h / 2, y + k2 / 2)
    k4 = h * f(eqn, x + h, y + k3)

    y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x += h
    result.append((x, y))

print(x, y)
