def get_path(orbits, source):
    o = source
    path = [source]
    while o != 'COM':
        o = orbits[o]
        path.append(o)
    return list(reversed(path))

orbits = {}
for l in [line.split(')') for line in open('input', 'r').read().splitlines()]:
    orbits[l[1]] = l[0]
count = 0
your_orbit = orbits['YOU']
santa_orbit = orbits['SAN']
your_path = get_path(orbits, your_orbit)
santa_path = get_path(orbits, santa_orbit)
while your_path[0] == santa_path[0]:
    your_path.remove(your_path[0])
    santa_path.remove(santa_path[0])
print(len(your_path) + len(santa_path))
