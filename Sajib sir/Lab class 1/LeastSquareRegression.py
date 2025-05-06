import math
# print(math.log(2))
n = input('n: ')
x = list(map(int, input().split()))
y = list(map(int, input().split()))

sum_x =  sum(x)
sum_y =  sum(y)
summation = 0
# print(math.sumprod(x, y))
sum_x_multiply_y = sum(map(lambda x, y: x*y, x , y ))
sum_x1_square = sum(map(lambda x: x * x, x))
# print(sum_x_multiply_y)

b = 