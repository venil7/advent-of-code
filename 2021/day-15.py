from collections import defaultdict
from heapq import heappop, heappush
import math


# file_name = "data/test.txt"
file_name = "data/day-15.txt"

Map = list[list[int]]
Coord = tuple[int, int]  # row,col


def get_map() -> Map:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    return [[int(s) for s in line.strip()] for line in lines]


def dijkstra(mp: Map, frm: Coord, to: Coord) -> int:
    visited = set(frm)
    weights = defaultdict(lambda: math.inf)
    weights[frm] = 0
    queue = []
    heappush(queue, (0, frm))
    while (to not in visited) or len(queue) > 0:
        (_, current) = heappop(queue)
        if current in visited:
            continue
        neighbours = unvisited_neighbours(mp, current, visited)

        for neighbour in neighbours:
            (r, c) = neighbour
            weight = weights[current] + mp[r][c]
            weights[neighbour] = min(weights[neighbour], weight)
            heappush(queue, (weights[neighbour], neighbour))

        visited.add(current)
    return weights[to]


def valid_coord(mp: Map, coord: Coord) -> bool:
    (rows, cols) = len(mp), len(mp[0])
    (row, col) = coord
    return row >= 0 and row < rows and col >= 0 and col < cols


def unvisited_neighbours(mp: Map, coord: Coord, visited: set[Coord]) -> list[Coord]:
    (row, col) = coord
    coords = [
        (row-1, col),
        (row, col-1),
        (row, col+1),
        (row+1, col),
    ]
    return [c for c in coords if valid_coord(mp, c) and c not in visited]


def calc(coord: Coord, orig_map: Map) -> int:
    (rows, cols) = len(orig_map), len(orig_map[0])
    (row, col) = coord
    (origrow, origcol) = row % rows, col % cols
    (rowadd, coladd) = row // rows, col // cols
    res = (orig_map[origrow][origcol] + rowadd + coladd)
    return res % 9 if res > 9 else res


def times_map(mp: Map,  factor: int) -> Map:
    (rows, cols) = len(mp), len(mp[0])
    return [[calc((row, col), mp) for col in range(cols*factor)] for row in range(rows*factor)]


def fifteen1():
    mp = get_map()
    (rows, cols) = len(mp), len(mp[0])
    print((rows, cols))
    print(dijkstra(mp, (0, 0), (rows-1, cols-1)))


def fifteen2():
    mp = get_map()
    mp = times_map(mp, 5)
    (rows, cols) = len(mp), len(mp[0])
    print((rows, cols))
    print(dijkstra(mp, (0, 0), (rows-1, cols-1)))


# fifteen1()
fifteen2()
