current_floor = 0

with open('input') as f:
    content = f.readlines()[0]

for i in content:
    if i == '(':
        current_floor += 1
    elif i == ')':
        current_floor -= 1

print('Floor: ' + str(current_floor))

