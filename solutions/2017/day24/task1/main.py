

def read_input():
    cs = set()
    with open('input', 'r') as f:
        for line in f:
            l, r = line.strip().split('/')
            cs.add((int(l), int(r)))
    return cs


def find_strongest(components, required_pins=0,  strength=0):
    strengths = [strength]
    for c in components:
        if c[0] == required_pins or c[1] == required_pins:
            pins = c[0] if c[1] == required_pins else c[1]
            strengths.append(find_strongest(components - {c}, pins, strength + c[0] + c[1]))
    return max(strengths)


components = read_input()
strongest = find_strongest(components)
print(strongest)
