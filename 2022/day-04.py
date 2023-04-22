import os

file_name = "{dir}/data/day-04.txt".format(dir=os.path.dirname(__file__))


def items() -> list[str]:
    with open(file_name, "rt") as file:
        return [item
                for item
                in file.read().splitlines()]


def expand_range(range_str: str) -> set[int]:
    start, end = map(int, range_str.split('-'))
    return set(range(start, end+1))


def subsets(items: list[str]) -> int:
    ranges = [item.split(",") for item in items]
    ranges = [tuple(map(expand_range, pair)) for pair in ranges]
    return sum([1 for left, right in ranges if left.issubset(right) or right.issubset(left)])


def overlaps(items: list[str]) -> int:
    ranges = [item.split(",") for item in items]
    ranges = [tuple(map(expand_range, pair)) for pair in ranges]
    return sum([1 for left, right in ranges if len(left.intersection(right)) > 0])


print(subsets(items()))
print(overlaps(items()))
