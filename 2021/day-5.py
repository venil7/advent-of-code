from itertools import repeat

file_name = "data/day_five.txt"
# file_name = "data/test.txt"

Coord = tuple[int, int]
Line = tuple[Coord, Coord]


def rng(frm, to) -> range:
    if frm == to:
        return repeat(frm)
    step = 1 if to > frm else -1
    return range(frm, to+step, step)


def parse_coord(s: str) -> Coord:
    coords = s.split(',')
    return(int(coords[0]), int(coords[1]),)


def parse_line(s: str) -> Line:
    coords = s.split('->')
    return (parse_coord(coords[0].strip()),
            parse_coord(coords[1].strip()),)


def get_lines() -> list[Line]:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    return [parse_line(line) for line in lines]


def max_coord(lines: list[Line]) -> Coord:
    (x, y,) = (0, 0)
    for ((x1, y1), (x2, y2),) in lines:
        x = max(x, x1, x2)
        y = max(y, y1, y2)
    return (x, y)


def draw_line(line: Line, plane: list[list[int]]):
    ((x1, y1), (x2, y2)) = line
    for (x, y) in zip(rng(x1, x2), rng(y1, y2)):
        plane[y][x] += 1


def calc_overlaps(plane: list[list[int]]):
    res = 0
    for row in plane:
        for cell in row:
            if cell > 1:
                res += 1
    return res


def valid_line(line: Line) -> bool:
    ((x1, y1), (x2, y2)) = line
    straight = (x1 == x2) or (y1 == y2)
    diag = abs(x1-x2) == abs(y1-y2)
    return straight or diag


def five1():
    lines = get_lines()
    (cols, rows) = max_coord(lines)
    plane = [[0 for col in range(cols+1)] for row in range(rows+1)]
    lines = [line for line in lines if valid_line(line)]
    for line in lines:
        draw_line(line, plane)
    res = calc_overlaps(plane)
    return res


print(five1())
