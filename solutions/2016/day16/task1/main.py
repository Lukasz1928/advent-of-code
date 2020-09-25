

def read_input():
    with open('input', 'r') as f:
        return f.read().strip()


def checksum(d):
    csm = ""
    for i in range(0, len(d) - 1, 2):
        csm += "1" if d[i] == d[i + 1] else "0"
    if len(csm) % 2 == 0:
        return checksum(csm)
    return csm


def update_data(d):
    return d + "0" + "".join([str(1 - int(x)) for x in reversed(list(d))])


state = read_input()
length = 272
while len(state) < length:
    state = update_data(state)
cksm = checksum(state[:length])
print(cksm)
