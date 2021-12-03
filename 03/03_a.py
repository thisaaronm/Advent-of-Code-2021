data = []
with open('03_puzzle_input.txt') as f:
    for i in f:
        data.append(i.strip())

g = []
e = []

i = 0
while i < len(data[0]):
    zero = 0
    one  = 0

    for d in data:
        if int(d[i]) == 0:
            zero += 1
        
        if int(d[i]) == 1:
            one += 1
    
    if zero > one:
        g.append(0)
        e.append(1)
    else:
        g.append(1)
        e.append(0)
    
    i += 1

gamma_bin = ''.join(list(map(str, g)))
gamma_dec = int(gamma_bin, 2)

epsilon_bin = ''.join(list(map(str, e)))
epsilon_dec = int(epsilon_bin, 2)

power_consumption = (gamma_dec * epsilon_dec)
print(power_consumption)