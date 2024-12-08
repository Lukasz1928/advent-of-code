from collections import defaultdict


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
            if is_in_grid(anitnode1 := (loc1[0] + diff[0], loc1[1] + diff[1]), size):
                antinodes.add(anitnode1)
            if is_in_grid(anitnode2 := (loc2[0] - diff[0], loc2[1] - diff[1]), size):
                antinodes.add(anitnode2)

result = len(antinodes)
print(result)
