def f(x):
    return 14 * (x**2) + (41*x)-14

# eqn = "14x2+41x-14"

a, b, n = map(float, input().split())

i = 0
x0 = 0
while i < n:
    x1 = a
    x2 = b
    x0 = (a + b) / 2

    f1 = f(x1)
    f2 = f(x2)
    f0 = f(x0)
    print(f"{x1} {x2}")
    if abs(f0) < 1e-6:
        print(x0)
        break

    if f0 * f1 < 0:
        b = x0
    else:
        a = x0
    i += 1

if i == n:
    print(x0)
