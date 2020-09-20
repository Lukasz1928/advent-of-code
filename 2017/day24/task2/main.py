

def read_input():
    cs = set()
    with open('input', 'r') as f:
        for line in f:
            l, r = line.strip().split('/')
            cs.add((int(l), int(r)))
    return cs


min_length = 1
strongest = -1


def find_strongest(components, required_pins=0,  strength=0, length=0):
    global min_length, strongest
    if length > min_length:
        strongest = strength
        min_length = length
    if strength > strongest and length == min_length:
        strongest = strength
    for c in components:
        if c[0] == required_pins or c[1] == required_pins:
            pins = c[0] if c[1] == required_pins else c[1]
            find_strongest(components - {c}, pins, strength + c[0] + c[1], length + 1)


components = read_input()
find_strongest(components)
print(strongest)
