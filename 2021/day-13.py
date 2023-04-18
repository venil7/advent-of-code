import pprint
import re


pp = pprint.PrettyPrinter(indent=4)

# file_name = "data/test.txt"
file_name = "data/day-13.txt"

Coord = tuple[int, int]
Fold = tuple[str, int]
Paper = list[list[bool]]


def get_paper(lst: list[Coord]) -> Paper:
    (max_x, max_y) = (
        max([x for (x, _) in lst]),
        max([y for (_, y) in lst])
    )
    coords = set(lst)
    return [[((x, y) in coords) for x in range(max_x+1)] for y in range(max_y+1)]


def parse_coords(s: str) -> Coord:
    [x, y] = s.strip().split(",")
    return (int(x), int(y))


def parse_fold(s: str) -> Fold:
    res = re.search(".*(x|y)=(\d+)$", s)
    return (res[1], int(res[2]))


def get_data() -> tuple[list[Coord], list[Fold]]:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    split = lines.index("\n")
    coords = [parse_coords(s) for s in lines[0:split]]
    folds = [parse_fold(s) for s in lines[split+1:]]

    return (coords, folds)


def fold(paper: Paper, f: Fold) -> Paper:
    (dir, line) = f
    if dir == 'x':
        return fold_x(paper, line)
    if dir == 'y':
        return fold_y(paper, line)


def safe_list_get(paper: Paper, coord: Coord):
    (x, y) = coord
    try:
        return paper[y][x]
    except IndexError:
        return False


def fold_y(paper: Paper, line: int) -> Paper:
    (max_x, _) = (len(paper[0]), len(paper))
    folded = [[paper[y][x] or safe_list_get(paper, (x, line+(line-y)))
               for x in range(max_x)] for y in range(0, line)]
    return folded


def fold_x(paper: Paper, line: int) -> Paper:
    (_, max_y) = (len(paper[0]), len(paper))
    folded = [[paper[y][x] or safe_list_get(paper, (line+(line-x), y))
               for x in range(0, line)] for y in range(max_y)]
    return folded


def num_dots(paper: Paper) -> int:
    return sum([1 if y else 0 for x in paper for y in x])


def pretty_print(paper: Paper):
    (max_x, max_y) = (len(paper[0]), len(paper))
    pp.pprint((max_x, max_y))
    npaper = [['#' if n else ' ' for n in row]for row in paper]
    for row in npaper:
        line = ''.join(row)
        print(line)
    # pp.pprint(npaper)
    # print(num_dots(paper))


def thirteen1():
    (coords, folds) = get_data()
    paper = get_paper(coords)
    paper = fold(paper, folds[0])
    print(num_dots(paper))


def thirteen2():
    (coords, folds) = get_data()
    paper = get_paper(coords)
    for fold_instruction in folds:
        paper = fold(paper, fold_instruction)
    pretty_print(paper)


# thirteen1()
thirteen2()
