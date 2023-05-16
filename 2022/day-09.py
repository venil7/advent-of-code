import os

file_name = "{dir}/data/day-09.txt".format(dir=os.path.dirname(__file__))


def parse_steps(s: str) -> list[tuple[int, int]]:
    direction, steps = s.split(" ")
    steps = int(steps)
    if direction == "R":
        return [(1, 0) for _ in range(steps)]
    if direction == "L":
        return [(-1, 0) for _ in range(steps)]
    if direction == "U":
        return [(0, 1) for _ in range(steps)]
    if direction == "D":
        return [(0, -1) for _ in range(steps)]


def steps() -> list[tuple[int, int]]:
    with open(file_name, "rt") as file:
        steps = [parse_steps(line) for line in file.read().splitlines()]
        return [step for sublist in steps for step in sublist]


def touching(p1: tuple[int, int], p2: tuple[int, int]) -> bool:
    return abs(p1[0] - p2[0]) <= 1 and abs(p1[1] - p2[1]) <= 1


def keep_up(head:  tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    if touching(head, tail):
        return tail

    xdiff = head[0] - tail[0]
    ydiff = head[1] - tail[1]

    # if in same column or longer distance by Y axis
    if xdiff == 0 or abs(xdiff) < abs(ydiff):
        return (head[0], head[1] - 1 if ydiff > 0 else head[1] + 1)

    # if in same row or longer distance by X axis
    if ydiff == 0 or abs(xdiff) > abs(ydiff):
        return (head[0] - 1 if xdiff > 0 else head[0] + 1, head[1])


def calc_all_tail_movements(steps: list[tuple[int, int]]) -> int:
    head, tail = (0, 0), (0, 0)
    tail_movements = set()
    tail_movements.add(tail)
    for (x, y) in steps:
        head = (head[0] + x, head[1] + y)
        tail = keep_up(head, tail)
        tail_movements.add(tail)
    return len(tail_movements)


def keep_up_test():
    assert keep_up((0, 0), (0, 0)) == (0, 0)
    assert keep_up((0, 0), (1, 0)) == (1, 0)
    assert keep_up((0, 0), (0, 1)) == (0, 1)

    assert keep_up((10, 10), (0, 10)) == (9, 10)
    assert keep_up((10, 10), (10, 0)) == (10, 9)

    assert keep_up((0, 0), (0, 10)) == (0, 1)
    assert keep_up((0, 0), (10, 0)) == (1, 0)

    assert keep_up((4, 3), (2, 4)) == (3, 3)
    assert keep_up((4, 2), (3, 0)) == (4, 1)


keep_up_test()
print(calc_all_tail_movements(steps()))
