import math
# file_name = "data/test.txt"
file_name = "data/ten.txt"

closing: dict[str, tuple[str, int]] = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137),
}
opening: set[str] = {'(', '{', '[', '<'}


def get_lines() -> list[str]:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def parse(line: str) -> tuple[str, int]:
    stack = []
    for s in line:
        if s in opening:
            stack.append(s)
        if s in closing:
            (o, score) = closing[s]
            if o == stack[-1]:
                stack.pop()
                continue
            else:
                return ('error', score)
    return complete(stack)


def complete(stack: list[str]) -> tuple[str, int]:
    scores: dict[str, int] = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    score = 0
    compl = stack.copy()
    compl.reverse()
    # brackets = [closing[bracket][0] for bracket in compl if bracket in closing]
    for bracket in compl:
        score = score * 5 + scores[bracket]

    return ('incomplete', score)


def ten1():
    lines = get_lines()
    results = [parse(line) for line in lines]
    return (sum([r[1] for r in results if r[0] == 'error']))


def ten2():
    lines = get_lines()
    results = [parse(line) for line in lines]
    res = [s[1] for s in results if s[0] == 'incomplete']
    res.sort()
    return res[int((len(res)-1)/2)]


print(ten1())
print(ten2())
