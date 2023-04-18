import copy


file_name = "data/day_three.txt"
# file_name = "data/test.txt"


def parse_binary(s: str) -> list[int]:
    return [int(c) for c in list(s) if c != '\n']


def number_from_binary(binary: list[int]) -> int:
    as_string = "".join(str(i) for i in binary)
    return int(as_string, 2)


def pos(i: int) -> int:
    return 1 if i > 0 else 0


def neg(i: int) -> int:
    return 1 if i < 0 else 0


def most_common(acc: list[int]) -> list[int]:
    return [pos(i) for i in acc]


def least_common(acc: list[int]) -> list[int]:
    return [neg(i) for i in acc]


def calc_acc(binaries: list[list[int]]) -> list[int]:
    binary_len = len(binaries[0])
    acc = [0] * binary_len
    for binary in binaries:
        for i in range(binary_len):
            if binary[i] == 1:
                acc[i] += 1
            elif binary[i] == 0:
                acc[i] -= 1
    return acc


def three1():
    with open(file_name, "rt") as file:
        binaries = [parse_binary(line) for line in file.readlines()]
    acc = calc_acc(binaries)
    gamma = number_from_binary(most_common(acc))
    epsil = number_from_binary(least_common(acc))

    return gamma * epsil


def rating(binaries: list[list[int]], get_bit: any) -> int:
    filtered = copy.deepcopy(binaries)
    width = len(binaries[0])
    for i in range(width):
        if len(filtered) == 1:
            return number_from_binary(filtered[0])
        else:
            acc = calc_acc(filtered)
            bit = get_bit(acc[i])
            filtered = list(filter(lambda binary: binary[i] == bit, filtered))
    return number_from_binary(filtered[0])


def three2():
    with open(file_name, "rt") as file:
        binaries = [parse_binary(line) for line in file.readlines()]

        def oxigen_bit(n): return 1 if n >= 0 else 0
        def scrubber_bit(n): return 0 if n >= 0 else 1

        oxygen = rating(binaries, oxigen_bit)
        scrubber = rating(binaries, scrubber_bit)
        return oxygen * scrubber


print(three1())
print(three2())
