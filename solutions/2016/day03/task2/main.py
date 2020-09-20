
def is_valid(t):
    return t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]


with open('input', 'r') as f:
    inp = [tuple(int(x) for x in l.split()) for l in f]
values = [x[0] for x in inp] + [x[1] for x in inp] + [x[2] for x in inp]
triangles = [(values[i], values[i + 1], values[i + 2]) for i in range(0, len(values), 3)]

valid_count = len([t for t in triangles if is_valid(t)])
print(valid_count)
