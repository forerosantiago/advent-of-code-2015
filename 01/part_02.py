current_floor = 0
pos = 0

with open('input') as f:
    content = f.readlines()[0]

for i in content:
    pos += 1
    if i == '(':
        current_floor += 1
    elif i == ')':
        current_floor -= 1

    if current_floor == -1:
        print('Position: ' + str(pos))
        break



