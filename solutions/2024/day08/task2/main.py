from collections import defaultdict
from math import gcd


def read_input() -> tuple[dict[str, list[tuple[int, int]]], tuple[int, int]]:
    d = defaultdict(list)
    height = 0
    width = 0
    with open('input', 'r') as f:
        for line_idx, line in enumerate(f.readlines()):
            height = line_idx
            for col_idx, elem in enumerate(line.strip()):
                width = col_idx
                if elem != '.':
                    d[elem].append((line_idx, col_idx))
    return dict(d), (height, width)


def is_in_grid(item: tuple[int, int], size: tuple[int, int]) -> bool:
    return 0 <= item[0] <= size[0] and 0 <= item[1] <= size[1]


items, size = read_input()
antinodes = set()
for key, locations in items.items():
    for loc1_idx, loc1 in enumerate(locations):
        for loc2 in locations[loc1_idx + 1:]:
            diff = loc1[0] - loc2[0], loc1[1] - loc2[1]
            diff_gcd = gcd(diff[0], diff[1])
            unit_diff = diff[0] // diff_gcd, diff[1] // diff_gcd
            unit_multiplier = 0
            while is_in_grid(anitnode := (loc1[0] + unit_diff[0] * unit_multiplier, loc1[1] + unit_diff[1] * unit_multiplier), size):
                antinodes.add(anitnode)
                unit_multiplier += 1
            unit_multiplier = 1
            while is_in_grid(anitnode := (loc1[0] - unit_diff[0] * unit_multiplier, loc1[1] - unit_diff[1] * unit_multiplier), size):
                antinodes.add(anitnode)
                unit_multiplier += 1

result = len(antinodes)
print(result)
