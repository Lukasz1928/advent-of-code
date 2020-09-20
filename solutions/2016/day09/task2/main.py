import re

with open('input', 'r') as f:
    file = f.read().strip()


def length(word):
    if '(' not in word:
        return len(word)
    if word.startswith('('):
        p = "\((\\d+)x(\\d+)\)(.*)"
        m = re.match(p, word)
        a = int(m.group(1))
        b = int(m.group(2))
        rest = m.group(3)
        return b * length(rest[:a]) + length(rest[a:])
    else:
        first_part_pattern = "(\\w*)(.*)"
        m = re.match(first_part_pattern, word)
        first_part = m.group(1)
        remainder = m.group(2)
        return len(first_part) + length(remainder)


result = length(file)
print(result)
