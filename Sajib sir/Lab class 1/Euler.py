import Equation_Parser as ep


def f(x):
    return 3 * x * x + 1


# x0, y0, h = map(float, input().split())

x0, y0, h, final = map(float, input().split())
# print(f"{x0} {y0} {h}")

print(f"xi = {x0} yi = {y0}")
for _ in range(50):
    y1 = y0 + (h * f(x0))
    x0 = x0 + h
    y0 = y1
    print(f"xi = {x0} yi = {y1}")
    if x0 == final:
        break
