course = []
with open('02_puzzle_input.txt') as f:
    for line in f:
        line_split = line.strip().split(' ')
        course.append([line_split[0], int(line_split[1])])

x = 0
y = 0
z = 0
for d in course:
    if d[0] == 'forward':
        x += d[1]
        y += (z * d[1])
        print(f'x = {x}; y = {z * d[1]}')
    elif d[0] == 'down':
        z += d[1]
        print(f'z = {z}')
    elif d[0] == 'up':
        z -= d[1]
        print(f'z = {z}')
    else:
        print('doh')
        break

print(f'{x} * {y} = {x * y}')
