def count_orbits(orbits, source):
    o = source
    count = 0
    while o != 'COM':
        o = orbits[o]
        count += 1
    return count

orbits = {}
for l in [line.split(')') for line in open('input', 'r').read().splitlines()]:
    orbits[l[1]] = l[0]
count = 0
for o in orbits.keys():
    count += count_orbits(orbits, o)
print(count)
