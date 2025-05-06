import re


class EquationParser:
    def __init__(self, equation):
        self.equation = equation.replace(" ", "")
        self.coefficients = {}

    def parsePolynomial(self):
        terms = re.findall(r'([+-]?\d*)x(\d+)', self.equation)
        constant = re.search(r'=\s*([+-]?\d+)', self.equation)

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

            coefficient = int(coefficient)
            self.coefficients[variable] = coefficient

        if constant:
            self.coefficients['constant'] = int(constant.group(1))
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

# equation1 = "12a1 + 21a2 + 222a3 = 12"
# parser1 = EquationParser(equation1)
# parser1.parseSimul()

# a, b, c, constant = parser1.get_coefficients('a1', "a2", 'a3', 'constant')
# constant = parser1.get_coefficients('constant')[0]

# print(f"Coefficient of a: {a}")
# print(f"Coefficient of b: {b}")
# print(f"Coefficient of c: {c}")
# print(f"Constant: {constant}")

# print()

# equation2 = "88x4 + 7x3 + 8x2 + 9x1 = 10"
# parser2 = EquationParser(equation2)
# parser2.parsePolynomial()

# x4, x3, x2, x1, c = parser2.get_coefficients(4, 3, 2, 1, 0)

# print(f'Coefficient of \nx^4: {x4}\nx^3: {x3}\nx^2: {x2}\nx^1: {x1}\nConstant: {c}')


# Calculate derivative
# derivative_result = parser2.derivative()  # Call the derivative method

# Print the result
# print("Derivative:", parser2.derivative())