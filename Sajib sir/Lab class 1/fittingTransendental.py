import math
# print(math.log(2))
sum_x = 0
sum_x_square = 0
sum_y = 0
sum_x_into_y = 0

n = int(input('n: '))
for i in range(n):
    temp_x = float(input('x: '))
    temp_y = float(input('y: '))
    
    temp_x = math.log(temp_x)
    temp_y = math.log(temp_y)
    
    sum_x += temp_x
    sum_y += temp_y
    sum_x_square += (temp_x ** 2)
    sum_x_into_y += (temp_x * temp_y)

# print(f'{sum_x} {sum_y} {sum_x_square} {sum_x_into_y}')
b = ((n * sum_x_into_y ) - (sum_x * sum_y) ) / ((n * sum_x_square) - (sum_x ** 2)) 

a = math.exp((sum_y / n) - (b * (sum_x / n)))

print(f'y = {a} x ^ {b}')