file_name = "data/one.txt"
# file_name = "test.txt"


def one():
    with open(file_name, "rt") as file:
        depths = [int(s) for s in file.readlines()]
    res = 0
    for i in range(1, len(depths)-1):
        if depths[i] > depths[i-1]:
            res += 1
    print(res)


def two():
    window_size = 3
    with open(file_name, "rt") as file:
        depths = [int(s) for s in file.readlines()]
    sum_depths = [depths[i:i+window_size]
                  for i in range(len(depths)-window_size+1)]
    res = 0
    for i in range(1, len(sum_depths)):
        if sum(sum_depths[i]) > sum(sum_depths[i-1]):
            res += 1
    print(res)


one()
two()
