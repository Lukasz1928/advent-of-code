import re
from collections import deque


def read_input():
    with open('input', 'r') as f:
        raw_input = f.read().strip()
    m = re.match(r'(\d+) players; last marble is worth (\d+) points', raw_input)
    return int(m.group(1)), int(m.group(2))


players, last_marble_value = read_input()
last_marble_value *= 100

circle = deque([0])
scores = {p: 0 for p in range(players)}

current_player = 0

for marble in range(1, last_marble_value + 1):
    if marble % 23 != 0:
        circle.rotate(-1)
        circle.append(marble)
    else:
        circle.rotate(7)
        scores[current_player] += marble + circle.pop()
        circle.rotate(-1)
    current_player = (current_player + 1) % players

winning_score = max(scores.values())
print(winning_score)
