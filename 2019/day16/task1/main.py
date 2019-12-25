

def multiply(signal):
    r = []
    l = len(signal)
    base_pattern = [0, 1, 0, -1]
    for i in range(l):
        pattern = get_pattern(base_pattern, i, l)
        r.append(abs(sum(signal[j] * pattern[j] for j in range(l))) % 10)
    return r


def get_pattern(base, index, length):
    p = []
    for d in base:
        p.extend([d] * (index + 1))
    lp = p[1:]
    while len(lp) < length:
        lp.extend(p)
    if len(lp) >= length:
        return lp[:length]


signal = [int(x) for x in open('input', 'r').read()]
for _ in range(100):
    signal = multiply(signal)
print(''.join([str(x) for x in signal[:8]]))
