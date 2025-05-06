import Equation_Parser as ep
import dtrmnt as dtr

list_of_equation = []

n = int(input())
for i in range(n):
    eqn = input()
    prsr = ep.EquationParser(eqn)
    prsr.parseSimul()
    eqn1 = prsr.get_coefficients("x1", "x2", "x3", "constant")
    list_of_equation.append(list(eqn1))

# for i in list_of_equation:
#     print(i)

mtx = [[], [], []]

mtx[0] = list_of_equation[0]
mtx[1] = list_of_equation[1]
mtx[2] = list_of_equation[2]


D = dtr.GetDeterminant(mtx)
# print(D)
temp0 = mtx[0][0]
temp1 = mtx[1][0]
temp2 = mtx[2][0]

mtx[0][0] = mtx[0][3]
mtx[1][0] = mtx[1][3]
mtx[2][0] = mtx[2][3]
Da1 = dtr.GetDeterminant(mtx)
# print(Da1)

mtx[0][0] = temp0
mtx[1][0] = temp1
mtx[2][0] = temp2

# ____________________
temp0 = mtx[0][1]
temp1 = mtx[1][1]
temp2 = mtx[2][1]

mtx[0][1] = mtx[0][3]
mtx[1][1] = mtx[1][3]
mtx[2][1] = mtx[2][3]
Da2 = dtr.GetDeterminant(mtx)
# print(Da2)

mtx[0][1] = temp0
mtx[1][1] = temp1
mtx[2][1] = temp2

# ____________________
temp0 = mtx[0][2]
temp1 = mtx[1][2]
temp2 = mtx[2][2]

mtx[0][2] = mtx[0][3]
mtx[1][2] = mtx[1][3]
mtx[2][2] = mtx[2][3]
Da3 = dtr.GetDeterminant(mtx)
# print(Da3)

print(f"a1 = {Da1/D}")
print(f"a2 = {Da2/D}")
print(f"a3 = {Da3/D}")
