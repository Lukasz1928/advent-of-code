prog = [int(x) for x in open('input', 'r').read().split(',')]
prog[1] = 12
prog[2] = 2
for i in range(0, len(prog) - 3, 4):
    if prog[i] == 99:
        break
    prog[prog[i + 3]] = (prog[prog[i + 1]] + prog[prog[i + 2]]) if prog[i] == 1 else (prog[prog[i + 1]] * prog[prog[i + 2]])
print(prog[0])
