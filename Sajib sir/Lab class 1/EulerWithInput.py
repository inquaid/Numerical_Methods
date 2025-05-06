import re

def convert_eqn(eqn):
    eqn = eqn.replace(" ", "")
    
    eqn = re.sub(r'(\d+)([xy])', r'\1*\2', eqn)  
    
    for i in range(2, 6):  
        eqn = re.sub(r'([xy])' + str(i), r'\1**' + str(i), eqn)  

    return eqn



# input_eqn = "2x5 + 3xy + 4y2 + 5x3 + 6y4"
input_eqn = input()
converted_eqn = convert_eqn(input_eqn)

x = 2
y = 3

evaluated_eqn = converted_eqn.replace("x", str(x)).replace("y", str(y))

# print("Original eqn:", input_eqn)
# print("Converted eqn:", converted_eqn)

result = eval(evaluated_eqn)
print(f"Evaluated eqn (f(x={x}, y={y})): {result}")
