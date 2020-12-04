

def read_input():
    with open('input', 'r') as f:
        return [tuple(int(d) for d in l.strip().split(',')) for l in f]


def distance(p, q):
    return sum(abs(p[i] - q[i]) for i in range(len(p)))


coordinates = read_input()

distances = {p: {q: distance(p, q) for q in coordinates} for p in coordinates}
constellations = {p: {q for q in coordinates if distances[p][q] <= 3} for p in coordinates}

changed = True
while changed:
    changed = False
    for current in constellations.values():
        to_update = set()
        for elem in current:
            if len(constellations[elem] - current) > 0:
                to_update.update(constellations[elem])
                changed = True
        current.update(to_update)

unique_constellations = set(tuple(sorted(tuple(p))) for p in constellations.values())
result = len(unique_constellations)
print(result)
