import pprint
import re
from typing import Generator, Iterable


pp = pprint.PrettyPrinter(indent=4)

# file_name = "data/test.txt"
file_name = "data/day-14.txt"

Rule = tuple[str, str]
Rules = dict[str, str]
Polymer = dict[str, int]


def parse_rule(s: str) -> Rule:
    res = re.search("^([A-Z]{2}) \-> ([A-Z])$", s)
    return (res[1], res[2])


def get_data() -> tuple[str, Rules]:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    split = lines.index("\n")

    polymer = lines[0].strip()
    rules = [parse_rule(s.strip()) for s in lines[split+1:]]

    return (polymer, dict(rules))


def to_pairs(s: str) -> Iterable[str]:
    for i in range(len(s)-1):
        yield s[i:i+2]


def step(char_counts: Polymer, pair_counts: Polymer, rules: Rules) -> tuple[Polymer, Polymer]:
    res = {}
    for key in pair_counts.keys():
        new = rules[key]
        count = pair_counts[key]
        char_counts[new] = char_counts.get(new, 0) + count
        (pair1, pair2) = key[0]+new, new+key[1]
        res[pair1] = res.get(pair1, 0) + count
        res[pair2] = res.get(pair2, 0) + count

    return (char_counts, res)


def get_char_counts(polymer: str) -> Polymer:
    res = {}
    for c in polymer:
        res[c] = res.get(c, 0) + 1
    return res


def get_pair_counts(polymer: str) -> Polymer:
    res = {}
    for key in to_pairs(polymer):
        res[key] = res.get(key, 0) + 1
    return res


def max_min_diff(char_counts: Polymer) -> int:
    mn = min(char_counts.values())
    mx = max(char_counts.values())
    return mx - mn


def fourteen1():
    (polymer, rules) = get_data()
    char_counts = get_char_counts(polymer)
    pair_counts = get_pair_counts(polymer)
    # for i in range(10):
    for i in range(40):
        (char_counts, pair_counts) = step(char_counts, pair_counts, rules)
    print(max_min_diff(char_counts))


fourteen1()
