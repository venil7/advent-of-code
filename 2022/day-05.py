import os
import re


file_name = "{dir}/data/day-05.txt".format(dir=os.path.dirname(__file__))


def items() -> list[str]:
    with open(file_name, "rt") as file:
        return [item
                for item
                in file.read().splitlines()]


def rotate(matrix: list[list[any]]) -> list[list[any]]:
    return list(zip(*matrix[::-1]))


def extract_crates(items: list[str]) -> list[list[str]]:
    split = items.index('')
    crates = items[:split-1]
    crates = list(map(lambda item: list([*item]), crates))
    crates = list(filter(lambda row: row[0].isalnum(), rotate(crates)))
    crates = list(map(lambda stack: list(filter(
        lambda n: n.isalnum(), stack)), crates))
    return crates


def parse_instruction(text: str) -> tuple[int, int, int]:
    match = re.search(r'move (\d+) from (\d+) to (\d+)', text)
    return tuple(map(int, match.groups()))


def extract_instructions(items: list[str]) -> list[tuple[int, int, int]]:
    split = items.index('')
    instructions = items[split+1:]
    return list(map(parse_instruction, instructions))


def execute_istruction(
        inst: tuple[int, int, int], crates: list[list[str]]) -> list[list[str]]:
    num, frm, to = inst
    for _ in range(num):
        crates[to-1].append(crates[frm-1].pop())
    return crates


def follow_instructions1(items: list[str]) -> str:
    crates = extract_crates(items)
    instructions = extract_instructions(items)
    for inst in instructions:
        crates = execute_istruction(inst, crates)
    return "".join(map(lambda stack: stack[-1], crates))


print(follow_instructions1(items()))
