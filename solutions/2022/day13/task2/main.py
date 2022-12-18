from ast import literal_eval


def read_input() -> list:
    d = []
    with open('input', 'r') as f:
        for pair in f.read().split('\n\n'):
            l, r = pair.split('\n')
            d.extend([literal_eval(l), literal_eval(r)])
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


def sort(lsts):
    for idx1 in range(len(lsts)):
        for idx2 in range(idx1 + 1, len(lsts)):
            if not are_ordered(lsts[idx1], lsts[idx2]):
                lsts[idx1], lsts[idx2] = lsts[idx2], lsts[idx1]
    return lsts


data = read_input()

sig1 = [[2]]
sig2 = [[6]]

extended_data = data + [sig1, sig2]

sorted_data = sort(extended_data)

sigs = [idx for idx, elem in enumerate(sorted_data, start=1) if elem in [sig1, sig2]]
result = sigs[0] * sigs[1]
print(result)
