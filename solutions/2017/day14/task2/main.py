

def read_input():
    with open('input', 'r') as f:
        return f.read().strip()


def to_ints(s):
    return [ord(x) for x in s]


def transform(lst, length, pos):
    if length + pos < len(lst):
        lst[pos:pos+length] = reversed(lst[pos:pos+length])
    else:
        r1 = lst[pos:]
        len1 = len(r1)
        r2 = lst[:length - len1]
        r = list(reversed(r1 + r2))
        lst[pos:] = r[:len1]
        lst[:length - len1] = r[len1:]


def hash16(numbers):
    x = numbers[0]
    for n in numbers[1:]:
        x ^= n
    return x


def to_bin(h):
    bn = "".join([bin(int(d, 16))[2:].zfill(4) for d in h])
    return bn


def to_int_array(h):
    return [[1 if d == '1' else 0 for d in x] for x in h]


def knot_hash(s):
    lengths = to_ints(s) + [17, 31, 73, 47, 23]
    lst = list(range(256))
    skip = 0
    pos = 0
    its = 64
    for it in range(its):
        for l in lengths:
            transform(lst, l, pos)
            pos = (pos + l + skip) % 256
            skip += 1
    hashs = [hash16(lst[i:i + 16]) for i in range(0, 255, 16)]
    hs = "".join([hex(x)[2:].zfill(2) for x in hashs])
    return to_bin(hs)


def count_regions(hashs):
    to_visit = set([(x, y) for x in range(128) for y in range(128) if hashs[x][y] == 1])
    ns = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    regions = 0
    while len(to_visit) > 0:
        current = to_visit.pop()
        to_visit.add(current)
        regions += 1
        current_group_next = [current]
        while len(current_group_next) > 0:
            c = current_group_next.pop(0)
            if c not in to_visit:
                continue
            to_visit.remove(c)
            for n in ns:
                potential_ngh = (c[0] + n[0], c[1] + n[1])
                if potential_ngh in to_visit:
                    current_group_next.append(potential_ngh)
    return regions


key = read_input()
hashes = [knot_hash(key + "-" + str(i)) for i in range(128)]
int_hashes = to_int_array(hashes)

region_count = count_regions(int_hashes)
print(region_count)
