

def read_input():
    with open('input', 'r') as f:
        lines = [' ' + l.replace('\n', '') + ' ' for l in f]
    return [' ' * len(lines[0])] + lines + [' ' * len(lines[0])]


directions = ['up', 'down', 'left', 'right']


class Node:
    def __init__(self, raw_graph, loc):
        self.location = loc
        self.neighbours = {d: False for d in directions}
        self.intersection = False
        current = raw_graph[loc[0]][loc[1]]
        if current in {'-', '<', '>'}:
            self.neighbours['left'] = True
            self.neighbours['right'] = True
        elif current in {'|', 'v', '^'}:
            self.neighbours['up'] = True
            self.neighbours['down'] = True
        elif current == '+':
            self.neighbours['left'] = True
            self.neighbours['right'] = True
            self.neighbours['up'] = True
            self.neighbours['down'] = True
            self.intersection = True
        elif current in {'/', '\\'}:
            if current == '/':
                if raw_graph[loc[0]][loc[1] + 1] in {'-', '+', '<', '>'}:
                    self.neighbours['right'] = True
                    self.neighbours['down'] = True
                else:
                    self.neighbours['left'] = True
                    self.neighbours['up'] = True
            else:
                if raw_graph[loc[0]][loc[1] + 1] in {'-', '+', '<', '>'}:
                    self.neighbours['right'] = True
                    self.neighbours['up'] = True
                else:
                    self.neighbours['left'] = True
                    self.neighbours['down'] = True


class Cart:
    sign2dir = {'^': 'up',
                'v': 'down',
                '<': 'left',
                '>': 'right'}

    direction_change = {
        'up': {
            'left': 'left',
            'straight': 'up',
            'right': 'right'
        },
        'down': {
            'left': 'right',
            'straight': 'down',
            'right': 'left'
        },
        'left': {
            'left': 'down',
            'straight': 'left',
            'right': 'up'
        },
        'right': {
            'left': 'up',
            'straight': 'right',
            'right': 'down'
        }
    }

    moves = {'up': lambda x: (x[0] - 1, x[1]),
             'down': lambda x: (x[0] + 1, x[1]),
             'left': lambda x: (x[0], x[1] - 1),
             'right': lambda x: (x[0], x[1] + 1)}

    intersection_directions = ['left', 'straight', 'right']

    def __init__(self, location, direction_sign, graph):
        self.location = location
        self.direction = Cart.sign2dir[direction_sign]
        self.graph = graph
        self.intersection_number = 0
        self.active = True
        self.last_move_epoch = -1

    def move(self, epoch=-1):
        self.location = Cart.moves[self.direction](self.location)
        current_node = self.graph.nodes[self.location]
        if current_node.intersection:
            turn = Cart.intersection_directions[self.intersection_number]
            self.intersection_number = (self.intersection_number + 1) % 3
            self.direction = Cart.direction_change[self.direction][turn]
        elif not current_node.neighbours[self.direction]:  # it is impossible to go straight
            if self.direction in {'up', 'down'}:
                self.direction = 'left' if current_node.neighbours['left'] else 'right'
            else:
                self.direction = 'up' if current_node.neighbours['up'] else 'down'
        self.last_move_epoch = epoch


class Graph:
    def __init__(self, raw_graph):
        self.nodes = {}
        self.carts = []
        for row in range(len(raw_graph)):
            for col in range(len(raw_graph[row])):
                if raw_graph[row][col] != ' ':
                    self.nodes[(row, col)] = Node(raw_graph, (row, col))
                if raw_graph[row][col] in {'v', '^', '<', '>'}:
                    self.carts.append(Cart((row, col), raw_graph[row][col], self))


def step(g, epoch):
    g.carts = list(sorted(g.carts, key=lambda c: c.location))
    for cart in g.carts:
        if not cart.active:
            continue
        cart.move(epoch)
        loc = cart.location
        carts_on_loc = [c for c in g.carts if c.location == loc and c.active]
        if len(carts_on_loc) > 1:
            for c in carts_on_loc:
                c.active = False
        remaining_carts = [c for c in g.carts if c.active]
        if len(remaining_carts) == 1:
            last_cart = remaining_carts[0]
            if last_cart.last_move_epoch != epoch:
                last_cart.move()
            return last_cart.location
    return None


raw_input = read_input()
graph = Graph(raw_input)

last_cart_location = None
epoch = 0
while last_cart_location is None:
    last_cart_location = step(graph, epoch)
    epoch += 1
result = f"{last_cart_location[1] - 1},{last_cart_location[0] - 1}"
print(result)
