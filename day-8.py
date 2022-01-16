file_name = "data/eight.txt"


def parse(s: str) -> tuple[list[str], list[str]]:
    [a, b] = s.split('|')
    return ([c.strip() for c in a.split()],
            [c.strip() for c in b.split()])


def get_nums() -> list[tuple[list[str], list[str]]]:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    return [parse(s.strip()) for s in lines]


def eight1():
    nums = get_nums()
    res = 0
    for (_, num) in nums:
        for n in num:
            #  1  4  7  8
            if len(n) in [2, 3, 4, 7]:
                res += 1
    return res

#  00
# 1  2
# 1  2
#  33
# 4  5
# 4  5
#  66

# sectors digits
# 2       1
# 3       7
# 4       4
# 5       2,3,5
# 6       6,9,0
# 7       8


def decode(code: list[str]) -> list[set[str]]:
    [one] = [z for z in code if len(z) == 2]
    one = set(one)
    [four] = [z for z in code if len(z) == 4]
    four = set(four)
    [seven] = [z for z in code if len(z) == 3]
    seven = set(seven)
    [eight] = [z for z in code if len(z) == 7]
    eight = set(eight)

    mem = {}
    mem[0] = seven-one
    mem[2] = mem[5] = one
    mem[1] = mem[3] = four-one
    mem[4] = mem[6] = eight-four-mem[0]

    four_one = four | mem[0]
    [nine] = [z for z in code if len(z) == 6 if len(set(z)-four_one) == 1]
    nine = set(nine)

    mem[4] = eight-nine
    mem[6] = mem[6]-mem[4]

    six_zero = [set(z) for z in code if len(
        z) == 6 if set(z) != nine and len(eight-set(z)) == 1]

    [zero] = [z for z in six_zero if z | one == z]
    [six] = [z for z in six_zero if z | one == eight]

    mem[3] = eight - zero
    mem[1] = mem[1] - mem[3]
    mem[2] = eight - six
    mem[5] = mem[5] - mem[2]

    two = eight - mem[1] - mem[5]
    three = eight - mem[1] - mem[4]
    five = eight - mem[2]-mem[4]

    return [
        zero, one, two, three, four, five, six, seven, eight, nine
    ]


def solve(input: list[str], codes: list[set[str]]) -> int:
    res = [str(codes.index(set(i))) for i in input]
    return int(''.join(res))


def eight2():
    items = get_nums()
    res = 0
    for (left, right) in items:
        res += solve(right, decode(left))
    return res


print(eight1())
print(eight2())
