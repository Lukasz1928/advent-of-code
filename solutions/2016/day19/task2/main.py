from collections import deque


def read_input():
    with open('input', 'r') as f:
        return int(f.read().strip())


elf_count = read_input()
elfs = list(range(1, elf_count + 1))

left = deque(elfs[:len(elfs)//2])
right = deque(elfs[len(elfs)//2:])
while len(left) + len(right) != 1:
    first = left.popleft()
    if len(left) == len(right):
        left.pop()
    else:
        right.popleft()
    right.append(first)
    left.append(right.popleft())
result = (list(left) + list(right))[0]
print(result)
