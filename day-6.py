file_name = "data/six.txt"
# file_name = "data/test.txt"

cache = {}


def calc(days: int, rep_cycle: int) -> list[int]:
    if ((days, rep_cycle,)) in cache:
        return cache[(days, rep_cycle,)]
    cont = [6, 8] if rep_cycle == 0 else [rep_cycle-1]
    if days == 1:
        return cont
    res = [z for rc in cont for z in calc(days-1, rc)]
    cache[(days, rep_cycle,)] = res
    return res


def get_fish() -> list[int]:
    with open(file_name, "rt") as file:
        content = file.read()
    return [int(s.strip()) for s in content.split(',')]


def proliferate(days: int, fish: list[int]) -> list[int]:
    for _ in range(days):
        new_fish = []
        for i in range(len(fish)):
            days = fish[i]
            if days == 0:
                new_fish.append(8)
                fish[i] = (6)
            else:
                fish[i] = (days-1)
        fish += new_fish
    return fish


def six1(days: int):
    fish = get_fish()
    fish = proliferate(days, fish)
    return len(fish)


def six2(days: int):
    mem = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    fish_times = get_fish()
    for ft in fish_times:
        mem[ft] += 1
    for _ in range(days):
        m0 = mem[0]
        mem[0] = mem[1]
        mem[1] = mem[2]
        mem[2] = mem[3]
        mem[3] = mem[4]
        mem[4] = mem[5]
        mem[5] = mem[6]
        mem[6] = mem[7] + m0
        mem[7] = mem[8]
        mem[8] = m0
    res = 0
    for i in range(0, 9):
        res += mem[i]
    return res


# print((six1(80)))
print((six2(256)))
# print(len(calc(200, 1)))
