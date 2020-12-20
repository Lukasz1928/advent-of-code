import math
import re
from queue import PriorityQueue

import numpy as np


def read_input():
    with open('input', 'r') as f:
        groups = f.read().split('\n\n')
    ts = {}
    for grp in groups:
        lines = grp.split('\n')
        tile_id = int(re.match(r'Tile (\d+)', lines[0]).group(1))
        img_lines = lines[1:]
        img_arr = [[int(elem == '#') for elem in row.strip()] for row in img_lines]
        ts[tile_id] = np.asarray(img_arr)
    return ts


def get_transformed(tile):
    rots = [(tile, (None,))] + [(np.rot90(tile, k=c), (90 * c,)) for c in [1, 2, 3]]
    flips = [(np.flip(t[0], axis=a), t[1] + (a,)) for a in [0, 1] for t in rots]
    return {trans: val for val, trans in [(r[0], r[1] + (None,)) for r in rots] + flips}


def get_neighbors(tiles):
    keys = list(tiles.keys())
    neighbors = {k: set() for k in keys}
    for i, tid in enumerate(keys):
        for tid2 in keys[i + 1:]:
            if tid2 in neighbors[tid]:
                break
            for tr1 in tiles[tid].keys():
                for tr2 in tiles[tid2].keys():
                    if ((tiles[tid][tr1][0, :] == tiles[tid2][tr2][-1, :]).all() or
                            (tiles[tid][tr1][-1, :] == tiles[tid2][tr2][0, :]).all() or
                            (tiles[tid][tr1][:, 0] == tiles[tid2][tr2][:, -1]).all() or
                            (tiles[tid][tr1][:, -1] == tiles[tid2][tr2][:, 0]).all()):
                        neighbors[tid].add(tid2)
                        neighbors[tid2].add(tid)
    return neighbors


def get_matches(t1, t2, direction, fixed=False):
    tr1 = get_transformed(t1)
    tr2 = get_transformed(t2) if not fixed else {(None, None): t2}
    transfs = set()
    for i1 in tr1.keys():
        for i2 in tr2.keys():
            if direction == 'down' and (tr1[i1][-1, :] == tr2[i2][0, :]).all():
                transfs.add(i1)
            if direction == 'up' and (tr1[i1][0, :] == tr2[i2][-1, :]).all():
                transfs.add(i1)
            if direction == 'right' and (tr1[i1][:, -1] == tr2[i2][:, 0]).all():
                transfs.add(i1)
            if direction == 'left' and (tr1[i1][:, 0] == tr2[i2][:, -1]).all():
                transfs.add(i1)
    return transfs


def transform(im, transformation):
    im1 = np.rot90(im, k=transformation[0]) if transformation[0] is not None else im
    im2 = np.flip(im, axis=transformation[1]) if transformation[1] is not None else im1
    return im2


def nghs(loc, gsize):
    return [x for x in [(loc[0] + 1, loc[1]), (loc[0] - 1, loc[1]), (loc[0], loc[1] + 1), (loc[0], loc[1] - 1)] if 0 <= x[0] < gsize and 0 <= x[1] < gsize]


def count_filled_nghs(loc, g):
    s = 0
    for n in nghs(loc, len(g)):
        try:
            s += int(g[n[0]][n[1]] is not None)
        except IndexError:
            pass
    return s


def get_element_to_insert(g, loc, nghs_, unused):
    ns = [g[x][y] for (x, y) in nghs(loc, len(grid)) if g[x][y] is not None]
    return [x for x in unused if all([xx in nghs_[x] for xx in ns])][0]


def build_image(grid, tiles):
    img = [[None for _ in range(len(grid))] for _ in range(len(grid))]
    conf1 = get_matches(tiles[grid[0][0]], tiles[grid[1][0]], 'right')
    conf2 = get_matches(tiles[grid[0][0]], tiles[grid[0][1]], 'down')
    conf = conf1.intersection(conf2)
    print(conf1, conf2, conf)
    img1 = transform(tiles[grid[0][0]], list(conf)[0])
    img[0][0] = np.asarray(img1)
    # print(img1)
    for i in range(1, len(img)):
        c = get_matches(tiles[grid[0][i]], img[0][i - 1], 'left', True)
        print(len(c))
        img[0][i] = transform(tiles[grid[0][i]], c.pop())


tiles = read_input()
transformed_tiles = {tid: get_transformed(tile) for tid, tile in tiles.items()}
neighbors = get_neighbors(transformed_tiles)

grid_size = int(math.sqrt(len(tiles)))
grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
grid[0][0] = [tid for tid, ngh in neighbors.items() if len(ngh) == 2][0]
Q = PriorityQueue()
enqueued = set()
for n in nghs((0, 0), grid_size):
    Q.put((-count_filled_nghs(n, grid), n))
    enqueued.add(n)
unused = set(neighbors.keys()) - {grid[0][0]}
while not Q.empty():
    current = Q.get()[1]
    enqueued.remove(current)
    inserted = get_element_to_insert(grid, current, neighbors, unused)
    unused.remove(inserted)
    grid[current[0]][current[1]] = inserted
    for n in nghs(current, grid_size):
        if grid[n[0]][n[1]] is None and n not in enqueued:
            Q.put((-count_filled_nghs(n, grid), n))
            enqueued.add(n)

img = build_image(grid, tiles)
