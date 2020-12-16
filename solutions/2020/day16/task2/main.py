import functools


class ValueSet:
    def __init__(self, desc):
        l, r = desc.split(' or ')
        self.low1, self.high1 = [int(x) for x in l.split('-')]
        self.low2, self.high2 = [int(x) for x in r.split('-')]

    def __contains__(self, item):
        return self.high1 >= item >= self.low1 or self.high2 >= item >= self.low2


def read_input():
    with open('input', 'r') as f:
        text = f.read()
    segments = text.split('\n\n')
    ranges = {}
    for l in segments[0].split('\n'):
        n, r = l.split(': ')
        ranges[n] = ValueSet(r)
    ticket = [int(x) for x in segments[1].split('\n')[1].split(',')]
    tickets = [tuple(int(x) for x in line.split(',')) for line in segments[2].split('\n')[1:]]
    return ranges, ticket, tickets


ranges, my_ticket, tickets = read_input()
valid_tickets = [ticket for ticket in tickets if all([any(val in r for r in ranges.values()) for val in ticket])]
possible_values = {x: set(ranges.keys()) for x in range(len(valid_tickets[0]))}
for index in range(len(valid_tickets[0])):
    for ticket in valid_tickets:
        for param in ranges.keys():
            if ticket[index] not in ranges[param]:
                possible_values[index].remove(param)
mapping = {}
used = set()
for group in list(sorted(possible_values.items(), key=lambda x: len(x[1]))):
    name = (group[1] - used).pop()
    idx = group[0]
    used.add(name)
    mapping[name] = idx

result = functools.reduce(lambda acc, val: acc * val,
                          [my_ticket[i] for i in {v for k, v in mapping.items() if k.startswith('departure')}])
print(result)
