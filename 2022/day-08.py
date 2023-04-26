import os
import numpy as np


file_name = "{dir}/data/day-08.txt".format(dir=os.path.dirname(__file__))


def items() -> list[str]:
    with open(file_name, "rt") as file:
        return [item
                for item
                in file.read().splitlines()]


def grid() -> list[list[int]]:
    return [[int(digit) for digit in item] for item in items()]


def visible(grid: np.array, coord: tuple[int, int]) -> bool:
    y, x = coord
    val = grid[y, x]
    left = grid[y, 0:x]
    right = grid[y, x+1:]

    top = grid[0:y, x]
    bottom = grid[y+1:, x]

    visible_left = val > np.max(left, initial=0) or left.size == 0
    visible_right = val > np.max(right, initial=0) or right.size == 0  # !

    visible_top = val > np.max(top, initial=0) or top.size == 0
    visible_bottom = val > np.max(bottom, initial=0) or bottom.size == 0  # !

    # print((y, x), "--->", val)
    # print("left", left)
    # print("right", right)
    # print("top", top)
    # print("bottom", bottom)
    # print("-----", visible_left or visible_right or visible_top or visible_bottom)

    return visible_left or visible_right or visible_top or visible_bottom


def task1(grid: list[list[int]]) -> int:
    grid = np.array(grid)
    (height, width) = grid.shape
    # print(height, width)
    return sum([1 for y in range(height)
                for x in range(width)
                if visible(grid, (y, x))])


print(task1(grid()))
