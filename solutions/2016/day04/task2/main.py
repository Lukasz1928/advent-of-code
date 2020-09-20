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


def rotate(letter, count):
    significant_count = count % 26
    return chr((ord(letter) - ord('a') + significant_count) % 26 + ord('a'))


def encrypt_name(name, rots):
    newname = ""
    for l in name:
        if l == '-':
            newname += ' '
        else:
            newname += rotate(l, rots)
    return newname


real_rooms = []
with open('input', 'r') as f:
    for l in f:
        room = parse_line(l)
        if get_most_common_letters(room[0]) == room[2]:
            real_rooms.append(room)

encrypted_rooms = [(encrypt_name(r[0], r[1]), r[1]) for r in real_rooms]
storage_rooms = [x for x in encrypted_rooms if x[0].endswith('storage')]
north_pole_storage_rooms = [x for x in storage_rooms if 'north' in x[0] and 'pole' in x[0]]
print(north_pole_storage_rooms[0][1])
