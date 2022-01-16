import math
file_name = "data/nine.txt"


def get_field() -> list[list[int]]:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    return [[int(i) for i in list(s.strip())] for s in lines]


def get_or_default(field: list[list[int]], row: int, col: int, default: int = 10) -> int:
    if row < 0 or col < 0:
        return default
    if row >= len(field) or (len(field) > 0 and col >= len(field[0])):
        return default
    return field[row][col]


def low_spots(field: list[list[int]]) -> list[tuple[int, int]]:
    res = []
    for row in range(len(field)):
        for col in range(len(field[row])):
            current = field[row][col]
            north = get_or_default(field, row-1, col)
            south = get_or_default(field, row+1, col)
            west = get_or_default(field, row, col-1)
            east = get_or_default(field, row, col+1)
            if all([current < n for n in [north, south, west, east]]):
                res.append((row, col))
    return res


def nine1():
    field = get_field()
    res = [field[r][c] + 1 for (r, c) in low_spots(field)]
    print(sum(res))


def basin_size(field: list[list[int]], coords: tuple[int, int], visited: set[tuple[int, int]] = set({})) -> int:
    if coords in visited:
        return 0
    (row, col) = coords
    n = get_or_default(field, row, col)
    if n >= 9:
        return 0
    else:
        visited.add(coords)
        return 1 + sum([
            basin_size(field, (row, col+1), visited),
            basin_size(field, (row, col-1), visited),
            basin_size(field, (row+1, col), visited),
            basin_size(field, (row-1, col), visited),
        ])


def nine2():
    field = get_field()
    spots = low_spots(field)
    basin_sizes = [basin_size(field, coords) for coords in spots]
    basin_sizes.sort(reverse=True)
    res = math.prod(basin_sizes[0:3])
    print(res)


# nine1()
nine2()
