file_name = "data/seven.txt"


def get_crabs() -> list[int]:
    with open(file_name, "rt") as file:
        content = file.read()
    return [int(s.strip()) for s in content.split(',')]


def calc_steps(steps: int) -> int:
    return sum(range(1, steps+1))


def calc_shift(crabs: list[int], target: int) -> int:
    return sum(
        [calc_steps(abs(target-crab)) for crab in crabs]
    )


def seven():
    crabs = get_crabs()
    mn = min(crabs)
    mx = max(crabs)
    res = float('inf')
    for t in range(mn, mx+1):
        res = min(res,
                  calc_shift(crabs, t))
    return res


print(seven())
