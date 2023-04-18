Coord = tuple[int, int]

(MINX, MAXX, MINY, MAXY) = (185, 221, -122, -74)


def hits_trench(coord: Coord) -> bool:
    x, y = coord
    return x >= MINX and x <= MAXX and y >= MINY and y <= MAXY


def overshoot(coord: Coord) -> bool:
    x, y = coord
    return x >= MAXX or y >= MAXY


def step(coord: Coord, velocity: Coord) -> tuple[Coord, Coord]:
    x, y = coord
    vx, vy = velocity
    return (x+vx, y+vy), (vx-1 if vx > 0 else (vx+1 if vx < 0 else 0), vy-1)


def steps(velocity: Coord):
    coord = (0, 0)
    while True:
        coord, velocity = step(coord, velocity)
        yield coord


def try_velocity(velocity: Coord) -> int:
    maxy = 0
    for coord in steps(velocity):
        (_, y) = coord
        maxy = max(maxy, y)
        if hits_trench(coord):
            return maxy
        if overshoot(coord):
            return -1


def seventeen():
