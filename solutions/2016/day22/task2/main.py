# general solution seems almost impossible
# used approach is based on the input and likely won't work for other inputs

import re


def read_input():
    n = []
    with open('input', 'r') as f:
        for l in [x.strip() for x in f][2:]:
            m = re.match(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', l)
            x, y = int(m.group(1)), int(m.group(2))
            size = int(m.group(3))
            used = int(m.group(4))
            avail = int(m.group(5))
            use = int(m.group(6))
            n.append(((x, y), size, used, avail, use))
    return n


def can_be_moved(nodes, node, max_size):
    node_size = nodes[node][1]
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if abs(dx) + abs(dy) == 1:
                if node_size <= max_size:
                    return True
    return False


nodes = read_input()
nodes_dict = {x[0]: x[1:] for x in nodes}

empty_node = [x for x in nodes if x[2] == 0][0]
empty_node_size = empty_node[1]

start_node = (0, 0)
goal_node = max([x[0] for x in nodes if x[0][1] == 0], key=lambda x: x[0])
board_width = goal_node[0] + 1
board_height = len(nodes) // board_width
img = [[' '] * board_width for _ in range(board_height)]
for n in nodes:
    x, y = n[0]
    size, used, avail, use = n[1:]
    if used == 0:
        img[y][x] = '_'
    else:
        if can_be_moved(nodes_dict, (x, y), empty_node_size):
            img[y][x] = '.'
        else:
            img[y][x] = '#'
img[goal_node[1]][goal_node[0]] = 'G'
img[0][0] = 'X'
full_img = '\n'.join([''.join(i) for i in img])
# print(full_img)  # used to visualise the grid

# count steps up to reach the "wall"
steps_to_wall = 0
h = empty_node[0][1]
while img[h][empty_node[0][0]] != '#':
    h -= 1
    steps_to_wall += 1
steps_to_wall -= 1

# count steps left to go around the "wall"
steps_to_end_of_wall = 0
w = empty_node[0][0]
while img[h][w] == '#':
    w -= 1
    steps_to_end_of_wall += 1

steps_to_go_around_wall = 2

# count steps to second but last column
steps_to_target_column = board_width - w - 2

# count steps to first row
steps_to_target_row = h - 1

# steps required to end up to the left of target data
steps_to_reach_data = steps_to_wall + steps_to_end_of_wall + steps_to_go_around_wall + steps_to_target_column + steps_to_target_row

# moving data left requires going: right, down, left, left, up
steps_to_move_data_left_once = 5

steps_to_move_data_to_target = steps_to_move_data_left_once * (board_width - 2) + 1

result = steps_to_reach_data + steps_to_move_data_to_target
print(result)
