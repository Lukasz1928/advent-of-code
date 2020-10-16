import re
from collections import deque


def read_input():
    with open('input', 'r') as f:
        raw_input = f.read().strip()
    m = re.match(r'(\d+) players; last marble is worth (\d+) points', raw_input)
    return int(m.group(1)), int(m.group(2))


players, last_marble_value = read_input()

circle = deque([0])
scores = {p: 0 for p in range(players)}

current_marble_index = 0
current_player = 0

for marble in range(1, last_marble_value + 1):
    if marble % 23 != 0:
        new_position = (current_marble_index + 1) % len(circle) + 1
        circle.rotate(-new_position)
        circle.appendleft(marble)
        circle.rotate(new_position)
        current_marble_index = new_position
    else:
        index_to_remove = (current_marble_index - 7) % len(circle)
        scores[current_player] += marble + circle[index_to_remove]
        circle.rotate(-index_to_remove)
        circle.popleft()
        circle.rotate(index_to_remove)
        current_marble_index = index_to_remove
    current_player = (current_player + 1) % players

winning_score = max(scores.values())
print(winning_score)
