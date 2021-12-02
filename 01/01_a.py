number_list = []
with open('01_puzzle_input.txt') as nums:
    for num in nums:
        number_list.append(int(num.strip()))
        '''

        Note: TLDR: lexicographic order

        If we don't cast to integers, leaving them as strings,
        then when comparing values of different lengths, such as
        998 against 1013 (lines 304 and 305), the string '998' 
        evaluates as greater than the string '1013', because the 
        first character of the string '998', 9, is greater than 
        the first character of the string '1013', 1.

        Reference: https://stackoverflow.com/a/10863114
        '''

index    = 1
increase = 0
while index <= (len(number_list) - 1):
    
    if number_list[index - 1] < number_list[index]:
        increase += 1
        print(f'{number_list[index - 1]} < {number_list[index]}. Increase: {increase}')

    index += 1

print(f'\nTOTAL Increase: {increase}')