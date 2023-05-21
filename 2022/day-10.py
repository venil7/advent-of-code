import os

file_name = "{dir}/data/day-10.txt".format(dir=os.path.dirname(__file__))

Command = tuple[int]


def parse_command(s: str) -> Command:
    if s == "noop":
        return (0,)
    _, number = s.split(" ")
    return (0, int(number))


def commands() -> list[Command]:
    with open(file_name, "rt") as file:
        steps = [parse_command(line) for line in file.read().splitlines()]
        return steps


def task1():
    cycle, x = 0, 1
    signals = []
    for command in commands():
        for subcommand in command:
            cycle += 1
            if (cycle-20) % 40 == 0:
                signals.append(x*cycle)
            x += subcommand

    return sum(signals)


if __name__ == "__main__":
    print(task1())
