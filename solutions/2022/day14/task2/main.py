

def to_tuple(x: str) -> tuple[int, int]:
    l, r = x.split(',')
    return int(l), int(r)


def sign(x):
    return int(abs(x) / x) if x != 0 else 0


def read_input() -> tuple[set[tuple[int, int]], int]:
    pts = set()
    max_y = 0
    with open('input', 'r') as f:
        for line in f:
            tokens = line.strip().split(' -> ')
            prev = to_tuple(tokens[0])
            max_y = max(max_y, prev[1])
            pts.add(prev)
            for tkn in tokens[1:]:
                loc = to_tuple(tkn)
                max_y = max(max_y, loc[1])
                dx = sign(loc[0] - prev[0])
                dy = sign(loc[1] - prev[1])
                curr = prev
                while curr != loc:
                    curr = (curr[0] + dx, curr[1] + dy)
                    pts.add(curr)
                prev = loc
            pts.add(to_tuple(tokens[-1]))
    return pts, max_y


rocks, max_height = read_input()
floor_height = max_height + 2
sand = set()


def add_sand(r: set[tuple[int, int]], floor: int) -> bool:
    loc = (500, 0)
    directions = [(0, 1), (-1, 1), (1, 1)]
    while True:
        moved = False
        for direction in directions:
            _loc = (loc[0] + direction[0], loc[1] + direction[1])
            if (_loc not in r and _loc[1] < floor) and _loc not in sand:
                loc = _loc
                moved = True
                break
        if not moved:
            break
    sand.add(loc)
    return loc != (500, 0)


while add_sand(rocks, floor_height):
    pass


result = len(sand)
print(result)
