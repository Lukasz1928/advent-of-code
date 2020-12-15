from collections import defaultdict, deque


def read_input():
    with open('input', 'r') as f:
        return [int(x) for x in f.read().split(',')]


numbers = read_input()
turns = defaultdict(lambda: deque(maxlen=2))
counts = defaultdict(lambda: 0)
for i, n in enumerate(numbers):
    turns[n].append(i)
    counts[n] += 1
prev = numbers[-1]
delta = None
for turn in range(len(numbers), 2020):
    if counts[prev] == 1:
        current = 0
    else:
        current = turns[prev][-1] - turns[prev][-2]
    turns[current].append(turn)
    counts[current] += 1
    prev = current
print(prev)
