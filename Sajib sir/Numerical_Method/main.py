import EquationParser as ep

eqn = input()
# eqn = input()
# eqn = input()
prsr = ep.EquationParser(eqn)
prsr.parseSimul()

lst = {}
# lst[0] = [0, 0, 0, 0]
lst[0][0], lst[0][1], lst[0][2], lst[0][3] = prsr.get_coefficients('x1', 'x2', 'x3', 'constant')
print(lst)