import pprint
pp = pprint.PrettyPrinter(indent=4)


# file_name = "data/test.txt"
file_name = "data/eleven.txt"

Field = list[list[int]]
Coord = tuple[int, int]


def get_field() -> Field:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    return [[int(s) for s in line.strip()] for line in lines]


def increase(field: Field, coord: Coord) -> bool:
    (row, col) = coord
    if row < 0 or row >= len(field):
        return False
    if col < 0 or col >= len(field[0]):
        return False
    field[row][col] += 1
    return field[row][col] == 10


def get_flashes(field: Field) -> set[Coord]:
    flashes = set([])
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == 10:
                flashes.add((row, col))
    return flashes


def flash(field: Field, coord: Coord):
    (row, col) = coord
    # field

    if increase(field, (row-1, col-1)):
        flash(field, (row-1, col-1))

    if increase(field, (row-1, col)):
        flash(field, (row-1, col))

    if increase(field, (row-1, col+1)):
        flash(field, (row-1, col+1))

    if increase(field, (row, col+1)):
        flash(field, (row, col+1))

    if increase(field, (row+1, col+1)):
        flash(field, (row+1, col+1))

    if increase(field, (row+1, col)):
        flash(field, (row+1, col))

    if increase(field, (row+1, col-1)):
        flash(field, (row+1, col-1))

    if increase(field, (row, col-1)):
        flash(field, (row, col-1))


def reg_step(field: Field) -> set[Coord]:
    for row in range(len(field)):
        for col in range(len(field[row])):
            increase(field, (col, row))


def reset_field(field: Field):
    res = 0
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] >= 10:
                field[row][col] = 0
                res += 1
    return res


def rec_step(field: Field, flashes: set[Coord]):
    if len(flashes) == 0:
        return
    for (row, col) in flashes:
        # field[row][col] = 12
        flash(field, (row, col))
    # new_flashes = get_flashes(field)
    # return rec_step(field, new_flashes)


def step(field: Field) -> int:
    reg_step(field)
    flashes = get_flashes(field)
    rec_step(field, flashes)
    return reset_field(field)


def all_flash(field: Field) -> bool:
    return all([all([n == 0 for n in row]) for row in field])


def eleven1():
    field = get_field()
    res = 0
    for i in range(100):
        res += step(field)
    print(res)


def eleven2():
    field = get_field()
    res = 0
    while True:
        step(field)
        res += 1
        if (all_flash(field)):
            break
    print(res)


eleven1()
eleven2()
