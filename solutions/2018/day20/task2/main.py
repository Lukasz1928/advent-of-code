# that's not a general solution that will work for any input
# it assumes that every alternative path ends in the same place
import networkx as nx


def read_input():
    with open('input', 'r') as f:
        regex = f.read().strip()
    return regex[1:-1]


def move(loc, dir):
    moves = {'N': lambda x, y: (x, y + 1),
             'S': lambda x, y: (x, y - 1),
             'E': lambda x, y: (x + 1, y),
             'W': lambda x, y: (x - 1, y)}
    return moves[dir](*loc)


regex = read_input()
graph = nx.Graph()
locs = []
loc = (0, 0)
for direction in regex:
    if direction == '(':
        locs.append(loc)
    elif direction == ')':
        loc = locs.pop()
    elif direction == '|':
        loc = locs[-1]
    else:
        new_loc = move(loc, direction)
        graph.add_edge(loc, new_loc)
        loc = new_loc
shortest_paths = nx.single_source_shortest_path_length(graph, (0, 0))
lengths = shortest_paths.values()
lengths_at_least_1000 = [x for x in lengths if x >= 1000]
result = len(lengths_at_least_1000)
print(result)
