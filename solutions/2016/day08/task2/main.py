import re


def parse_instruction(i):
    pattern_rect = "rect (\\d+)x(\\d+)"
    m_rect = re.match(pattern_rect, i)
    if m_rect is not None:
        return "rect", int(m_rect.group(1)), int(m_rect.group(2))

    pattern_rc = "rotate column x=(\\d+) by (\\d+)"
    m_rc = re.match(pattern_rc, i)
    if m_rc is not None:
        return "rc", int(m_rc.group(1)), int(m_rc.group(2))

    pattern_rr = "rotate row y=(\\d+) by (\\d+)"
    m_rr = re.match(pattern_rr, i)
    if m_rr is not None:
        return "rr", int(m_rr.group(1)), int(m_rr.group(2))


def rect(d, w, h):
    for wi in range(w):
        for hi in range(h):
            d[hi][wi] = 1
    return d


def rc(d, c, rots):
    col = [d[i][c] for i in range(len(d))]
    new_col = col[len(col) - rots:] + col[:len(col) - rots]
    for i in range(len(d)):
        d[i][c] = new_col[i]
    return d


def rr(d, r, rots):
    row = d[r]
    new_row = row[len(row) - rots:] + row[:len(row) - rots]
    d[r] = new_row
    return d


def apply(d, i):
    instr = parse_instruction(i)
    if instr[0] == "rect":
        return rect(d, instr[1], instr[2])
    if instr[0] == "rc":
        return rc(d, instr[1], instr[2])
    if instr[0] == "rr":
        return rr(d, instr[1], instr[2])
    return d


def print_display(d):
    for r in d:
        for i in r:
            print("#" if i == 1 else " ", end='')
        print()


with open('input', 'r') as f:
    instrs = [l.strip() for l in f]

size = [50, 6]
display = [[0] * size[0] for _ in range(size[1])]

for i in instrs:
    display = apply(display, i)

print_display(display)
