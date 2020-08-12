from collections import Counter


def read_input():
    with open('input', 'r') as f:
        return [x for x in f.read().strip().split(',')]


def remove_cancelling_moves(ms):
    c = Counter(ms)
    return {
        'n': c['n'] - c['s'],
        'ne': c['ne'] - c['sw'],
        'se': c['se'] - c['nw']
    }


def reduce_moves(ms):
    changed = True
    reduced = False
    while changed:
        changed = False
        if ms['n'] > 0:
            if ms['se'] > 0:
                m = min(ms['n'], ms['se'])
                ms['n'] = ms['n'] - m
                ms['se'] = ms['se'] - m
                ms['ne'] = ms['ne'] + m
                changed = True
            elif ms['ne'] < 0:
                m = min(ms['n'], -ms['ne'])
                ms['n'] = ms['n'] - m
                ms['ne'] = ms['ne'] + m
                ms['se'] = ms['se'] - m
                changed = True
        if ms['n'] < 0:
            if ms['ne'] > 0:
                m = min(-ms['n'], ms['ne'])
                ms['n'] = ms['n'] + m
                ms['ne'] = ms['ne'] - m
                ms['se'] = ms['se'] + m
                changed = True
            elif ms['se'] < 0:
                m = min(-ms['n'], -ms['se'])
                ms['n'] = ms['n'] + m
                ms['se'] = ms['se'] + m
                ms['ne'] = ms['ne'] - m
                changed = True
        if ms['ne'] > 0:
            if ms['se'] < 0:
                m = min(ms['ne'], -ms['se'])
                ms['ne'] = ms['ne'] - m
                ms['se'] = ms['se'] + m
                ms['n'] = ms['n'] + m
                changed = True
        if ms['ne'] < 0:
            if ms['se'] > 0:
                m = min(-ms['ne'], ms['se'])
                ms['ne'] = ms['ne'] + m
                ms['se'] = ms['se'] - m
                ms['n'] = ms['n'] - m
                changed = True
        if ms['se'] > 0:
            if ms['ne'] < 0:
                m = min(ms['se'], -ms['ne'])
                ms['se'] = ms['se'] - m
                ms['ne'] = ms['ne'] + m
                ms['n'] = ms['n'] - m
                changed = True
        if ms['se'] < 0:
            if ms['ne'] > 0:
                m = min(-ms['se'], ms['ne'])
                ms['se'] = ms['se'] + m
                ms['ne'] = ms['ne'] - m
                ms['n'] = ms['n'] + m
                changed = True
        if changed:
            reduced = True
    return ms, reduced


moves = read_input()
max_len = len(moves) + 1
max_dist = 0

for i in range(max_len):
    c = True
    short_moves = remove_cancelling_moves(moves[:i])
    while c:
        short_moves, c = reduce_moves(short_moves)
    length = sum([abs(x) for x in short_moves.values()])
    if length > max_dist:
        max_dist = length

print(max_dist)
