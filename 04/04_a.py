def get_data(puzzle_input):

    boards = []
    with open(puzzle_input) as f:
        lines = f.readlines()

        drawn = list(map(int, lines[0].strip().split(',')))

        board = []
        for line in lines[1:]:
            if len(line.strip()) != 0:
                row = line.strip().replace('  ', ' ').split(' ')
                board.append(list(map(int, row)))

            if len(board) == 5:
                boards.append(board)
                board = []

    return drawn, boards


def create_boards(board):
    board_h = board
    board_v = []

    new_row = []
    index = 0
    while index < 5:
        for row in board:
            new_row.append(row[index])

        board_v.append(new_row)
        new_row = []
        index +=1
    
    return board_h, board_v


def check_numbers(drawn, board, board_num):
    count = 0
    while count < len(drawn):
        for num in drawn:
            # print(f'Drawing number: {num}')
            for row in board:
                if num in row:
                    # print(f'Found number: {num}')
                    row.remove(num)

                if len(row) == 0:
                    # print(F'BINGO! Board {board_num}, draw number {count}, winning number {num}')
                    return [board_num, count, num]

            count += 1


def sum_remaining(board):
    list_of_remaining = []
    
    for i in board:
        for num in i:
            list_of_remaining.append(num)
    
    return sum(list_of_remaining)


def check_boards(draw, boards):
    b = []
    board_num = 0
    for board in boards:
        b.append(check_numbers(draw, board, board_num))
        board_num += 1
    
    board_number, draw_count, winning_number = sorted(b, key=lambda b : b[1])[0]
    remaining_numbers = boards[board_number]
    sum_of_remaining = sum_remaining(remaining_numbers)

    return board_number, draw_count, winning_number, remaining_numbers, sum_of_remaining


def main(puzzle_input):
    draw, boards = get_data(puzzle_input)

    boards_h = []
    boards_v = []
    for board in boards:
        bh, bv = create_boards(board)
        boards_h.append(bh)
        boards_v.append(bv)

    bh_board_number, bh_draw_count, bh_winning_number, bh_remaining_numbers, bh_sum_of_remaining = check_boards(draw, boards_h)
    # print(bh_board_number, bh_draw_count, bh_winning_number, bh_remaining_numbers, bh_sum_of_remaining)

    bv_board_number, bv_draw_count, bv_winning_number, bv_remaining_numbers, bv_sum_of_remaining = check_boards(draw, boards_v)
    # print(bv_board_number, bv_draw_count, bv_winning_number, bv_remaining_numbers, bv_sum_of_remaining)

    if bh_draw_count < bv_draw_count:
        type = 'HORIZONTAL'
        brdn = bh_board_number
        drwc = bh_draw_count
        winn = bh_winning_number
        remn = bh_remaining_numbers
        sumn = bh_sum_of_remaining
    else:
        type = 'VERTICAL'
        brdn = bv_board_number
        drwc = bv_draw_count
        winn = bv_winning_number
        remn = bv_remaining_numbers
        sumn = bv_sum_of_remaining


    print(f'''
The winning board number was {type} board {brdn + 1} (index {brdn}),
getting BINGO on draw number {drwc + 1} (index {drwc}).
The winning number was {winn}!

The remaining numbers on board {brdn + 1} (index {brdn}) are:

    {remn}

which have a sum of {sumn}. When multiplied by 
the winning number, {winn}, return a value of {sumn * winn}
''')


if __name__ == '__main__':
    main('04_puzzle_input.txt')