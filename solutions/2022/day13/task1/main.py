from ast import literal_eval


def read_input() -> list[tuple[list, list]]:
    d = []
    with open('input', 'r') as f:
        for pair in f.read().split('\n\n'):
            l, r = pair.split('\n')
            d.append((literal_eval(l), literal_eval(r)))
    return d


def are_ordered(l: int | list, r: int | list) -> bool | None:
    l_int = isinstance(l, int)
    r_int = isinstance(r, int)
    if l_int and r_int:
        if l == r:
            return None
        return l < r
    if l_int and not r_int:
        return are_ordered([l], r)
    if not l_int and r_int:
        return are_ordered(l, [r])
    length = min(len(l), len(r))
    for a, b in zip(l[:length], r[:length]):
        if (ordered := are_ordered(a, b)) is not None:
            return ordered
    if len(l) == len(r):
        return None
    return len(l) < len(r)


data = read_input()
result = sum(idx for idx, pair in enumerate(data, start=1) if are_ordered(*pair))
print(result)
