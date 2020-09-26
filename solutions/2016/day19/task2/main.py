

def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


elf_count = read_input()
elfs = list(range(1, elf_count + 1))
index = 0
l = len(elfs)
while l > 1:
    remove_idx = (index + l // 2) % l
    index = (index + 1) % l
    del elfs[remove_idx]
    l -= 1
    if l % 1000 == 0:
        print(l)
result = elfs[0]
print(result)
