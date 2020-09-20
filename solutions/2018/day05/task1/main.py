
def read_input():
    with open('input', 'r') as f:
        i = f.read()
    return i


def remove_parts(s, p):
    ns = ""
    prev_idx = 0
    for idx in p:
        ns += s[prev_idx:idx]
        prev_idx = idx + 2
    ns += s[prev_idx:]
    return ns


p = read_input()
removed = True
while removed:
    to_remove = []
    i = 0
    l = len(p) - 1
    while i < l:
        if p[i].upper() == p[i + 1].upper() and p[i] != p[i + 1]:
            to_remove.append(i)
            i += 2
        else:
            i += 1
    removed = len(to_remove) > 0
    p = remove_parts(p, to_remove)

result = len(p)
print(result)