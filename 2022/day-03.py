import os

file_name = "{dir}/data/day-03.txt".format(dir=os.path.dirname(__file__))


def rucksack_items() -> list[str]:
    with open(file_name, "rt") as file:
        return [item
                for item
                in file.read().splitlines()]


def split(item: str) -> tuple[str, str]:
    return (item[:len(item)//2], item[len(item)//2:])


def common_chars(strings: tuple[str, ...]) -> set[str]:
    common = set(strings[0])
    for string in strings[1:]:
        common.intersection_update(set(string))
    return common


def item_score(s: set[str]) -> int:
    c = s.pop()
    if c.isupper():
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1


def all_common_items(items: list[tuple[str, str]]) -> list[str]:
    return sum([item_score(common_chars(item))
                for item
                in items])


def common_per_three_group(items: list[str]) -> int:
    groups = [tuple(items[i:i+3])
              for i
              in range(0, len(items), 3)]

    return sum([item_score(common_chars(group))
                for group
                in groups])


print(all_common_items([split(item) for item in rucksack_items()]))
print(common_per_three_group(rucksack_items()))
