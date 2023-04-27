import os
import numpy as np
from typing import Callable


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


def visibility_calc(grid: np.array, val: int, coord: tuple[int, int], next: Callable):
    (height, width) = grid.shape
    (y, x) = coord
    if y < 0 or y >= height:
        return 0
    if x < 0 or x >= width:
        return 0
    current = grid[y, x]
    if current >= val:
        return 1
    return 1 + visibility_calc(grid, val, next(y, x), next)


def visibility_index(grid: np.array, coord: tuple[int, int]):
    (y, x) = coord
    def next_up(y, x): return (y-1, x)
    def next_down(y, x): return (y+1, x)
    def next_left(y, x): return (y, x-1)
    def next_right(y, x): return (y, x+1)

    return np.prod([visibility_calc(grid, grid[y, x], next_up(y, x),  next_up),
                    visibility_calc(
                        grid, grid[y, x], next_down(y, x),  next_down),
                    visibility_calc(
                        grid, grid[y, x], next_left(y, x),  next_left),
                    visibility_calc(grid, grid[y, x], next_right(y, x),  next_right)])


def task2(grid: list[list[int]]) -> int:
    grid = np.array(grid)
    (height, width) = grid.shape
    return max([visibility_index(grid, (y, x)) for y in range(height)
                for x in range(width)])


print(task2(grid()))
