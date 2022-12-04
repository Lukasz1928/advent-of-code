def read_input() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    raw_input = []
    with open('input', 'r') as f:
        for line in f:
            l, r = line.split(',')
            l1, l2 = l.split('-')
            r1, r2 = r.split('-')
            raw_input.append(((int(l1), int(l2)), (int(r1), int(r2))))
    return raw_input


def overlap(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return not (b[0] > a[1] or a[0] > b[1])


data = read_input()
result = len([1 for elf in data if overlap(*elf)])
print(result)
