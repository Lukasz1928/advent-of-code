from collections import deque


def read_input():
    with open('input', 'r') as f:
        raw_input = f.read()
    p1, p2 = raw_input.split('\n\n')
    p1_cards = deque([int(x) for x in p1.split('\n')[1:]])
    p2_cards = deque([int(x) for x in p2.split('\n')[1:]])
    return p1_cards, p2_cards


p1, p2 = read_input()

while p1 and p2:
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1.extend([c1, c2])
    elif c1 < c2:
        p2.extend([c2, c1])

score = sum(x * idx for idx, x in enumerate(reversed(p1 + p2), start=1))
print(score)
