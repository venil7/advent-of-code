from functools import reduce


file_name = "data/day-16.txt"
# file_name = "data/test.txt"


def get_lines() -> list[str]:
    with open(file_name, "rt") as file:
        return [line.strip() for line in file.readlines()]


SUM = 0
PRODUCT = 1
MIN = 2
MAX = 3
LITERAL = 4
GT = 5
LT = 6
EQ = 7


def prod(*nums: list[int]) -> int:
    return reduce(lambda a, b: a*b, nums)


def sum(*nums: list[int]) -> int:
    return reduce(lambda a, b: a+b, nums)


# def id(*x: list[int]) -> int: return x[0]
def mmin(*xs: list[int]) -> int: return min(list(xs))
def mmax(*xs: list[int]) -> int: return max(list(xs))
def gt(a, b) -> int: return 1 if a > b else 0
def lt(a, b) -> int: return 1 if a < b else 0
def eq(a, b) -> int: return 1 if a == b else 0


ops = (sum, prod, mmin, mmax, None, gt, lt, eq)


def parser(line: str) -> tuple[int, int]:
    bits = (int(bit) for ch in line for bit in "{:04b}".format(int(ch, 16)))
    pos = 0
    ver = 0

    def read_bits(num: int) -> int:
        nonlocal pos
        pos += num
        return int(''.join([str(next(bits)) for _ in range(num)]), 2)

    def read_packet() -> int:
        nonlocal ver
        ver += read_bits(3)
        typ = read_bits(3)
        if typ == LITERAL:
            val = 0
            while True:
                delim = read_bits(1)
                val = (val << 4) | read_bits(4)
                if delim == 0:
                    break
            return val
        else:
            length_typ = read_bits(1)
            args = ()
            if length_typ == 0:
                bits_to_read = read_bits(15)
                pos_finish = pos + bits_to_read
                while pos < pos_finish:
                    args += (read_packet(),)
            else:
                packets_to_read = read_bits(11)
                for _ in range(packets_to_read):
                    args += (read_packet(),)
            return ops[typ](*args)

    res = read_packet()
    return ver, res


def sixteen1():
    lines = get_lines()
    for line in lines:
        print(parser(line))


sixteen1()
