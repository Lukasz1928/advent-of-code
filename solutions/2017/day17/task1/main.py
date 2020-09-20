

def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


steps = read_input()

buffer = [0]
pos = 0
next_number = 1
inserts = 2017
for i in range(inserts):
    pos = (pos + steps) % len(buffer)
    buffer = buffer[:pos + 1] + [next_number] + buffer[pos+1:]
    next_number += 1
    pos = (pos + 1) % len(buffer)

result = buffer[(pos + 1) % len(buffer)]
print(result)
