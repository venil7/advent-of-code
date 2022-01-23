# file_name = "data/test.txt"
file_name = "data/day-16.txt"


def get_raw() -> str:
    with open(file_name, "rt") as file:
        return file.read()


# version, bits consumed, remainder str, list of children
ReadResult = tuple[int, int, str, list]


LITERAL = 4


def hex2bin(s: str) -> str:
    num = int(s, 16)
    binary = "{0:b}".format(num)
    while len(binary) % 4 != 0:
        binary = '0'+binary
    return binary


def bin2dec(s: str) -> int:
    return int(s, 2)


def parse(binary: str) -> list[ReadResult]:
    (ver, typ, data) = bin2dec(binary[0:3]),  bin2dec(binary[3:6]), binary[6:]

    if typ == LITERAL:
        (_, bits_consumed, remainder, children) = literal(ver, data)
        return [(ver, 6+bits_consumed, remainder, children)]
    else:
        children = operator(data)
        (_, bits_consumed, remainder, _) = reduce(children)
        return [(ver, 6+bits_consumed, remainder, children)]


def literal(ver: int, bits: str) -> ReadResult:
    res = ''
    for i in range(0, len(bits), 5):
        res += bits[i+1:i+5]
        if bits[i] == '0':
            break
    val = bin2dec(res)
    return (ver, len(res) + (i+1), bits[i*5+5:], [])


def reduce(children: list[ReadResult]) -> ReadResult:
    (ver, bits, rem) = 0, 0, ''
    for (v, b, r, _) in children:
        ver += v
        bits += b
        rem = r
    return (ver, bits, rem, children)


def operator(bits: str) -> list[ReadResult]:
    length_type_id = bits[0]
    readabale_data = bits[1:]
    res = []
    if length_type_id == '0':
        num_bits_to_read = bin2dec(readabale_data[:15])
        data = readabale_data[15:15+num_bits_to_read]
        remainder = readabale_data[15+num_bits_to_read:]
        total_bits_consumed = 0
        while num_bits_to_read > 0 and total_bits_consumed < num_bits_to_read:
            (ver, bits_consumed, data, children) = reduce(parse(data))
            total_bits_consumed += bits_consumed
            res.append((ver, 1 + 15 + num_bits_to_read, remainder, children))
    elif length_type_id == '1':
        num_sub_packets = bin2dec(bits[1:12])
        data = bits[12:]
        for i in range(num_sub_packets):
            (ver, bits_consumed, data, children) = reduce(parse(data))
            res.append((ver, 1 + 11 + bits_consumed, data, children))
    return res


# def sum_ver(ops: ReadResult) -> int

def sixteen1():
    bin = hex2bin(get_raw())
    res = parse(bin)
    (v, _, _, _) = reduce(res)
    print(v)
    pass


sixteen1()
