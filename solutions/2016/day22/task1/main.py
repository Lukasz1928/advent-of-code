import re


def read_input():
    n = []
    with open('input', 'r') as f:
        for l in [x.strip() for x in f][2:]:
            m = re.match(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', l)
            x, y = int(m.group(1)), int(m.group(2))
            size = int(m.group(3))
            used = int(m.group(4))
            avail = int(m.group(5))
            use = int(m.group(6))
            n.append(((x, y), size, used, avail, use))
    return n


nodes = read_input()
count = 0
for i, n in enumerate(nodes):
    for j, m in enumerate(nodes):
        if i != j and 0 < n[2] <= m[3]:
            count += 1
print(count)
