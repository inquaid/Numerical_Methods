import Equation_Parser as ep
import sys
list_of_equation = []
# list_of_equation.append(1)
# list_of_equation[0] = 12
# print(list_of_equation)
n = int(input())
for i in range(n):
    eqn = input()
    prsr = ep.EquationParser(eqn)
    prsr.parseSimul()
    equation_1 = prsr.get_coefficients('x1', 'x2', 'x3', 'constant')
    list_of_equation.append(list(equation_1))

list_of_equation.sort(key=lambda x : (abs(x[0]), abs(x[1]), abs(x[2])), reverse=True)

for i in list_of_equation:
    print(i) 
print()


if list_of_equation[1][0] != 0:
    div2 = list_of_equation[0][0] / list_of_equation[1][0]
else:
    div2 = 0
if list_of_equation[2][0] != 0:
    div3 = list_of_equation[0][0] / list_of_equation[2][0]
else:
    div3 = 0
# sys.exit()

   
for i in range(len(list_of_equation[0])):
    if div2 != 0:
        list_of_equation[1][i] =  list_of_equation[0][i] - (list_of_equation[1][i] * div2)
    
    if div3 != 0:
        list_of_equation[2][i] =  list_of_equation[0][i] - (list_of_equation[2][i] * div3)

list_of_equation.sort(key=lambda x : (abs(x[0]), abs(x[1]), abs(x[2])), reverse=True)

print()
for i in list_of_equation:
    print(i) 
    
if list_of_equation[2][1] != 0:
    div4 = list_of_equation[1][1] / list_of_equation[2][1]
else:
    div4 = 0
    
if div4 != 0:
    for i in range(len(list_of_equation[0])):
        list_of_equation[2][i] = list_of_equation[1][i] - (list_of_equation[2][i] * div4)

list_of_equation.sort(key=lambda x : (abs(x[0]), abs(x[1]), abs(x[2])), reverse=True)

print()
for i in list_of_equation:
    print(i) 


#.................................................................

if list_of_equation[1][2] != 0:
    div4 = list_of_equation[2][2] / list_of_equation[1][2]
else:
    div4 = 0
    
if div4 != 0:
    for i in range(len(list_of_equation[0])):
        list_of_equation[1][i] = list_of_equation[2][i] - (list_of_equation[1][i] * div4)

list_of_equation.sort(key=lambda x : (abs(x[0]), abs(x[1]), abs(x[2])), reverse=True)

print()
for i in list_of_equation:
    print(i) 
    
    

#.................................................................

if list_of_equation[0][2] != 0:
    div4 = list_of_equation[2][2] / list_of_equation[0][2]
else:
    div4 = 0
    
if div4 != 0:
    for i in range(len(list_of_equation[0])):
        list_of_equation[0][i] = list_of_equation[2][i] - (list_of_equation[0][i] * div4)

list_of_equation.sort(key=lambda x : (abs(x[0]), abs(x[1]), abs(x[2])), reverse=True)

print()
for i in list_of_equation:
    print(i) 
    
#..................................................................
if list_of_equation[0][1] != 0:
    div4 = list_of_equation[1][1] / list_of_equation[0][1]
else:
    div4 = 0
    
if div4 != 0:
    for i in range(len(list_of_equation[0])):
        list_of_equation[0][i] = list_of_equation[1][i] - (list_of_equation[0][i] * div4)

list_of_equation.sort(key=lambda x : (abs(x[0]), abs(x[1]), abs(x[2])), reverse=True)

print()
for i in list_of_equation:
    print(i) 

x = list_of_equation[0][3] / list_of_equation[0][0]
y = list_of_equation[1][3] / list_of_equation[1][1]
z = list_of_equation[2][3] / list_of_equation[2][2]


print(f'\nx = {x}\ny = {y}\nz = {z}')