def get_data(puzzle_input):
    data = []
    with open(puzzle_input) as f:
        for i in f:
            data.append(i.strip())
    return data


def get_common(data, index, rating):
    zero = 0
    one  = 0
    for d in data:
        if d[index] == '0':
            zero += 1
        else:
            one += 1

    if zero > one:
        if rating == 'oxygen':
            common = 0
        else:
            common = 1
    else:
        if rating == 'oxygen':
            common = 1
        else:
            common = 0
    
    c = [d for d in data if d[index] == str(common)]
    
    if len(c) == 1:
        print(c[0])
    return c


def get_rating(data, rating):
    new_data = data
    index    = 0
    while len(new_data) > 1:
        new_data = get_common(new_data, index, rating)
        if len(new_data) == 1:
            return new_data[0]
        index += 1


def life_support(oxygen, c02):
    o = int(oxygen, 2)
    c = int(c02, 2)
    return (o * c)


def main():
    data = get_data('03_puzzle_input.txt')
    oxygen_rating = get_rating(data, 'oxygen')
    c02_rating = get_rating(data, 'c02')
    life_support_rating = life_support(oxygen_rating, c02_rating)
    
    print(life_support_rating)


if __name__ == '__main__':
    main()