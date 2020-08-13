import re
from copy import copy


def read_input():
    with open('input', 'r') as f:
        return [x.strip() for x in f.read().split(',')]


def to_names(lst):
    return [chr(x + ord('a')) for x in lst]


def apply(lst, instr):
    if instr.startswith("s"):
        slen = int(instr[1:])
        return lst[-slen:] + lst[:-slen]
    elif instr.startswith("x"):
        m = re.match("x(\\d+)/(\\d+)", instr)
        pos1, pos2 = int(m.group(1)), int(m.group(2))
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
        return lst
    else:
        prog1 = instr[1]
        prog2 = instr[3]
        pos1 = lst.index(prog1)
        pos2 = lst.index(prog2)
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
        return lst


def phash(p):
    return "".join(p)


instrs = read_input()
programs_count = 16
progs = to_names(list(range(programs_count)))

prev_programs = {phash(progs)}
first_repeat_id = 0
while True:
    for instr in instrs:
        progs = apply(progs, instr)
    h = phash(progs)
    if h in prev_programs:
        break
    prev_programs.add(h)
    first_repeat_id += 1

period = 0
period_start_program = copy(progs)
while True:
    period += 1
    for instr in instrs:
        progs = apply(progs, instr)
    if progs == period_start_program:
        break
print("bb")
dance_repeats = 1000000000 - first_repeat_id
needed_additional_transforms = dance_repeats % period
for _ in range(needed_additional_transforms):
    for instr in instrs:
        progs = apply(progs, instr)

result = phash(progs)
print(result)
