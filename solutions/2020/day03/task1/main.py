
def read_input():
    with open('input', 'r') as f:
        return [l.strip() for l in f]


area_map = read_input()
slope = (3, 1)
trees = sum(area_map[y][(y//slope[1] * slope[0]) % len(area_map[0])] == '#'
            for y in range(0, len(area_map), slope[1]))
print(trees)
