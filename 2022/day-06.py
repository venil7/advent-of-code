import os
# import re


file_name = "{dir}/data/day-06.txt".format(dir=os.path.dirname(__file__))


def signal() -> list[str]:
    with open(file_name, "rt") as file:
        return file.read()


def is_signal(window: str) -> bool:
    return len(set(window)) == len(window)


def first_signal(signal: str, window_size=4) -> int:
    for i in range(0, len(signal)-window_size):
        window = signal[i:i+window_size]
        # print(i, window)
        if is_signal(window):
            return i+window_size
    return -1


print(first_signal(signal()))
