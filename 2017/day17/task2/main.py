

def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


steps = read_input()
steps = 3
pos = 0
next_number = 1
first_nonzero = 0
inserts = 9
for i in range(inserts):
    pos = (pos + steps) % (i + 1)
    if pos == 0:
        first_nonzero = i + 1
        print(i + 1)
    pos = (pos + 1) % (i + 1)

print(first_nonzero)
