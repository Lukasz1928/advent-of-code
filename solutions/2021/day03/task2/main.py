from collections import Counter


def read_input():
    with open('input', 'r') as f:
        return [l.strip() for l in f.readlines()]


def get_most_common(data, index):
    cnt = Counter([d[index] for d in data]).most_common()
    if len(cnt) == 1:
        return cnt[0][0], str(1 - int(cnt[0][0]))
    if cnt[0][1] == cnt[1][1]:
        return '1', '0'
    return cnt[0][0], cnt[1][0]


def calculate_rating(data, common_index):
    position = 0
    while len(data) != 1:
        mc = get_most_common(data, position)[common_index]
        data = [d for d in data if d[position] == mc]
        position += 1
    return int(data[0], 2)


data = read_input()
bit_count = len(data[0])
result = calculate_rating(data, 0) * calculate_rating(data, 1)
print(result)
