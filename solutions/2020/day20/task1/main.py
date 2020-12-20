import re
import numpy as np
import functools


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


tiles = read_input()
transformed_tiles = {tid: get_transformed(tile) for tid, tile in tiles.items()}
neighbors = get_neighbors(transformed_tiles)

corners = [tid for tid, val in neighbors.items() if len(val) == 2]
result = functools.reduce(lambda acc, val: acc * val, corners)
print(result)
