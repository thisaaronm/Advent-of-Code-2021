number_list = []
with open('01_puzzle_input.txt') as nums:
    for num in nums:
        number_list.append(int(num.strip()))

increase = 0
while len(number_list) >= 4:

    a = sum(number_list[:3])
    number_list.pop(0)
    b = sum(number_list[:3])

    if a < b:
        increase += 1
        print(f'{a} < {b}. Increase: {increase}')

print(f'\nTOTAL Increase: {increase}')
