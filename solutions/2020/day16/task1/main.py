
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


ranges, _, tickets = read_input()
ser = 0
for ticket in tickets:
    ser += sum([val for val in ticket if not any(val in r for r in ranges.values())])
print(ser)
