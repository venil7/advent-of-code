file_name = "data/day_four.txt"

Board = list[list[(int, bool)]]


def parse_board(lines: list[str]) -> Board:
    return [[(int(x), False) for x in line.split()] for line in lines]


def mark_number_in_board(board: Board, num: int) -> Board:
    return [[(cell[0], cell[1] or (cell[0] == num)) for cell in row] for row in board]


def check_winner(board: Board) -> bool:
    for row in board:
        if all(map(lambda cell: cell[1], row)):
            return True
    board_width = len(board)
    for i in range(board_width):
        if all(map(lambda cell: cell[1], [board[j][i] for j in range(board_width)])):
            return True
    return False


def sum_unmarked(board: Board) -> int:
    res = 0
    for row in board:
        for cell in row:
            if not cell[1]:
                res += cell[0]
    return res


def get_nums_and_boards():
    with open(file_name, "rt") as file:
        lines = file.readlines()
    nums = [int(n) for n in lines[0].split(',')]
    boards = [parse_board(lines[i+1:i+6]) for i in range(1, len(lines), 6)]
    return (nums, boards)


def four1():
    (nums, boards) = get_nums_and_boards()

    for num in nums:
        for i in range(len(boards)):
            boards[i] = mark_number_in_board(boards[i], num)
            if check_winner(boards[i]):
                return sum_unmarked(boards[i]) * num


def four2():
    (nums, boards) = get_nums_and_boards()
    winning_boards = [False for i in range(len(boards))]
    for num in nums:
        for i in range(len(boards)):
            boards[i] = mark_number_in_board(boards[i], num)
            winning_boards[i] = check_winner(boards[i])
            if all(winning_boards):
                return sum_unmarked(boards[i]) * num


print(four1())
print(four2())
