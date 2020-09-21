from hashlib import md5


def read_input():
    with open('input', 'r') as f:
        return f.read().strip()


def stretched_hash(s):
    t = s
    for _ in range(2017):
        t = hash(t)
    return t


def hash(s):
    m = md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()


def find_triple_digits(h):
    for i in range(len(h) - 2):
        if h[i] == h[i + 1] == h[i + 2]:
            return h[i]
    return None


def has_5_same_digits(h, digit):
    return (digit * 5) in h


def is_key(hashes, index):
    d = find_triple_digits(hashes[index])
    if d is None:
        return False
    for i in range(1, 1001):
        if has_5_same_digits(hashes[index + i], d):
            return True
    return False


salt = read_input()
index = 0
count = 0
hashes = [stretched_hash(salt + str(x)) for x in range(1001)]
while True:
    if is_key(hashes, index):
        count += 1
    if count == 64:
        break
    index += 1
    hashes.append(stretched_hash(salt + str(len(hashes))))

result = index
print(result)
