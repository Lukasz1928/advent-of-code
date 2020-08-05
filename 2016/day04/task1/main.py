import re
from collections import Counter


def parse_line(line):
    match = re.match("((?:\w+-?)+)-(\d+)\[(\w+)\]", line)
    name = match.group(1)
    id = int(match.group(2))
    checksum = match.group(3)
    return name, id, checksum


def get_most_common_letters(name):
    letters = Counter(name.replace("-", ""))
    counts = letters.most_common()
    sc = sorted(counts, key=lambda x: (-x[1], x[0]))
    return "".join([x[0] for x in sc[:5]])


ssum = 0
with open('input', 'r') as f:
    for l in f:
        room = parse_line(l)
        if get_most_common_letters(room[0]) == room[2]:
            ssum += room[1]
print(ssum)
