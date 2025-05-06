def func(x):
    return (x * x) - (4 * x) - 10

x1 = 4.0
x2 = 2.0

while abs(x2 - x1) >= 0.005:
    print(x2)
    x3 = x2 - ((func(x2) * (x2 - x1)) / (func(x2) - func(x1)))
    x1 = x2
    x2 = x3