import re


def read_input():
    with open('input', 'r') as f:
        return f.read().strip()


def count_garbage(d):
    in_garbage = False
    d = re.sub('!.', '', d)
    i = 0
    length = 0
    while i < len(d):
        if in_garbage:
            if d[i] == '>' and d[i - 1] != '!':
                in_garbage = False
            else:
                length += 1
            i += 1
        else:
            if d[i] == '<':
                in_garbage = True
            i += 1
    return length


raw_data = read_input()
garbage_length = count_garbage(raw_data)
print(garbage_length)
