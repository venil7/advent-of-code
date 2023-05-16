import os

file_name = "{dir}/data/day-09.txt".format(dir=os.path.dirname(__file__))

Coord = tuple[int, int]
Step = tuple[int, int]


def parse_steps(s: str) -> list[Step]:
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


def steps() -> list[Step]:
    with open(file_name, "rt") as file:
        steps = [parse_steps(line) for line in file.read().splitlines()]
        return [step for sublist in steps for step in sublist]


def touching(p1: tuple[int, int], p2: tuple[int, int]) -> bool:
    return abs(p1[0] - p2[0]) <= 1 and abs(p1[1] - p2[1]) <= 1


def keep_up(lead:  Coord, follow: Coord) -> tuple[int, int]:
    if touching(lead, follow):
        return follow

    xdiff = lead[0] - follow[0]
    ydiff = lead[1] - follow[1]

    # if in same column or longer distance by Y axis
    if xdiff == 0 or abs(xdiff) < abs(ydiff):
        return (lead[0], lead[1] - 1 if ydiff > 0 else lead[1] + 1)

    # if in same row or longer distance by X axis
    if ydiff == 0 or abs(xdiff) > abs(ydiff):
        return (lead[0] - 1 if xdiff > 0 else lead[0] + 1, lead[1])

    return (lead[0] - 1 if xdiff > 0 else lead[0] + 1,
            lead[1] - 1 if ydiff > 0 else lead[1] + 1)


def calc_tail_movements(steps: list[Step], length: int = 2) -> set[Coord]:
    rope = [(0, 0) for _ in range(length)]
    tail_movements = set()
    tail_movements.add(rope[-1])

    for (x, y) in steps:
        rope[0] = (rope[0][0] + x, rope[0][1] + y)
        for i in range(1, len(rope)):
            rope[i] = keep_up(rope[i - 1], rope[i])
        tail_movements.add(rope[-1])

    return tail_movements


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


def part1(steps: list[Step] = steps()):
    tail_movements = calc_tail_movements(steps)
    print(len(tail_movements))


def part2(steps: list[Step] = steps()):
    tail_movements = calc_tail_movements(steps, 10)
    print(len(tail_movements))


keep_up_test()

part1()
part2()
