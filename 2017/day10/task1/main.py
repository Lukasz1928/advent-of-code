

def read_input():
    with open('input', 'r') as f:
        return [int(x) for x in f.read().strip().split(',')]


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


lengths = read_input()
numbers = 256
skip = 0
lst = list(range(numbers))

pos = 0
for l in lengths:
    transform(lst, l, pos)
    pos = (pos + l + skip) % numbers
    skip += 1

result = lst[0] * lst[1]
print(result)
