import pprint
import copy

pp = pprint.PrettyPrinter(indent=4)

# file_name = "data/test.txt"
file_name = "data/day-12.txt"

Place = str
Route = tuple[Place, Place]
Map = dict[Place, set[Place]]


def single_use(p: Place) -> bool:
    return p.upper() != p


def parse_route(s: str) -> Route:
    [name1, name2] = s.split('-')
    return (name1, name2)


def get_routes() -> Map:
    with open(file_name, "rt") as file:
        lines = file.readlines()
    routes = [parse_route(line.strip()) for line in lines]
    dic = {}
    for (frm, to) in routes:
        dic[frm] = (dic[frm] | {to}) if frm in dic else {to}
        dic[to] = (dic[to] | {frm}) if to in dic else {frm}
    return dic


def walk(m: Map, umap: dict[Place, int], path:  tuple[Place] = ('start',)) -> set[tuple]:
    frm = path[-1]
    if frm == 'end':
        return {path}
    if frm not in m:
        return {()}

    res = set()
    dest = m[frm]

    for d in dest:
        if umap[d] < 1:
            continue
        umap1 = umap | {d: umap[d] - 1}
        res |= walk(m, umap1,  path + (d,))

    return res


def twelve1():
    routes = get_routes()
    umap = {k: (1 if single_use(k) else float('inf'))
            for k in routes.keys()}
    umap['start'] = 0
    all_paths = walk(routes, umap) - {()}
    print(len(all_paths))


def twelve2():
    routes = get_routes()
    umap = {k: (1 if single_use(k) else float('inf'))
            for k in routes.keys()}
    umap['start'] = 0

    res = set()
    for d in umap.keys():
        umap_copy = umap | {}
        if single_use(d) and d != 'start' and d != 'end':
            umap_copy |= {d: 2}
        res |= walk(routes, umap_copy) - {()}

    print(len(res))


twelve1()
twelve2()
