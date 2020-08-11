

def read_input():
    with open('input', 'r') as f:
        return [ord(x) for x in f.read().strip()]


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


lengths = read_input()
lengths += [17, 31, 73, 47, 23]

numbers = 256
lst = list(range(numbers))
skip = 0
pos = 0
its = 64
for it in range(its):
    for l in lengths:
        transform(lst, l, pos)
        pos = (pos + l + skip) % numbers
        skip += 1

hashes = [hash16(lst[i:i+16]) for i in range(0, 255, 16)]
hs = "".join([hex(x)[2:].zfill(2) for x in hashes])
print(hs)
