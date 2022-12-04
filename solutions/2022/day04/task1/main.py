def read_input() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    raw_input = []
    with open('input', 'r') as f:
        for line in f:
            l, r = line.split(',')
            l1, l2 = l.split('-')
            r1, r2 = r.split('-')
            raw_input.append(((int(l1), int(l2)), (int(r1), int(r2))))
    return raw_input


def contains(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1])


data = read_input()
result = len([1 for elf in data if contains(*elf)])
print(result)
