
def is_valid(t):
    return t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]


with open('input', 'r') as f:
    triangles = [tuple(int(x) for x in l.split()) for l in f]

valid_count = len([t for t in triangles if is_valid(t)])
print(valid_count)
