file_name = "data/two.txt"


def parse_step(s: str) -> tuple((str, int)):
    [step, amount] = s.split(' ')
    return (step, int(amount))


def two():
    [forward, depth] = [0, 0]
    with open(file_name, "rt") as file:
        steps = [parse_step(s) for s in file.readlines()]

    for (step, amount) in steps:
        if step == "forward":
            forward += amount
        elif step == "down":
            depth += amount
        elif step == "up":
            depth -= amount

    return forward * depth


def two_():
    [forward, aim, depth] = [0, 0, 0]
    with open(file_name, "rt") as file:
        steps = [parse_step(s) for s in file.readlines()]

    for (step, amount) in steps:
        if step == "forward":
            forward += amount
            depth += aim*amount
        elif step == "down":
            aim += amount
        elif step == "up":
            aim -= amount

    return forward * depth


print(two())
print(two_())
