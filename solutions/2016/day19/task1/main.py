

def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


elf_count = read_input()
elfs = list(range(1, elf_count + 1))
while len(elfs) > 1:
    if len(elfs) % 2 == 0:
        elfs = elfs[::2]
    else:
        elfs = elfs[2::2]
result = elfs[0]
print(result)
