from collections import Counter


def read_input():
    with open('input', 'r') as f:
        return [l.strip() for l in f.readlines()]


def get_params(data, index):
    cnt = Counter([d[index] for d in data]).most_common()
    return cnt[0][0], cnt[1][0]


data = read_input()
bit_count = len(data[0])
a, b = '', ''
for idx in range(bit_count):
    _a, _b = get_params(data, idx)
    a += _a
    b += _b
result = int(a, 2) * int(b, 2)
print(result)
