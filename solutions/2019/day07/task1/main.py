from copy import copy


def decode(inst):
    s = str(inst).zfill(5)
    p1 = s[2] == '0'
    p2 = s[1] == '0'
    p3 = s[0] == '0'
    op = int(s[3:])
    return p1, p2, p3, op

perms = []

def permutate(digits, current=""):
    if len(digits) == 0:
        perms.append(current)
    else:
        for digit in digits:
            permutate([x for x in digits if x != digit], current + digit)
permutate(['0', '1', '2', '3', '4'])

prog_ = [int(x) for x in open('input', 'r').read().split(',')]

m = -1
for index, perm in enumerate(perms):
    pout = []
    for thruster in range(5):
        prog = copy(prog_)
        i = 0
        pin = [int(perm[0]), 0] if thruster == 0 else [int(perm[thruster]), pout[len(pout) - 1]]
        while True:
            p1, p2, p3, op = decode(prog[i])
            if op == 99:  # end of program
                break
            if op == 1:  # addition
                prog[prog[i + 3]] = ((prog[prog[i + 1]] if p1 else prog[i + 1]) + (prog[prog[i + 2]] if p2 else prog[i + 2]))
                i += 4
            elif op == 2:  # multiplication
                prog[prog[i + 3]] = ((prog[prog[i + 1]] if p1 else prog[i + 1]) * (prog[prog[i + 2]] if p2 else prog[i + 2]))
                i += 4
            elif op == 3:  # read input
                prog[prog[i + 1]] = pin[0]
                pin.remove(pin[0])
                i += 2
            elif op == 4:  # write to output
                pout.append(prog[prog[i + 1]] if p1 else prog[i + 1])
                i += 2
            elif op == 5:  # jump if true
                if (prog[prog[i + 1]] if p1 else prog[i + 1]) != 0:
                    i = prog[prog[i + 2]] if p2 else prog[i + 2]
                else:
                    i += 3
            elif op == 6:  # jump if false
                if (prog[prog[i + 1]] if p1 else prog[i + 1]) == 0:
                    i = prog[prog[i + 2]] if p2 else prog[i + 2]
                else:
                    i += 3
            elif op == 7:  # less than
                prog[prog[i + 3]] = 1 if ((prog[prog[i + 1]] if p1 else prog[i + 1]) < (prog[prog[i + 2]] if p2 else prog[i + 2])) else 0
                i += 4
            elif op == 8:  # equals
                prog[prog[i + 3]] = 1 if ((prog[prog[i + 1]] if p1 else prog[i + 1]) == (prog[prog[i + 2]] if p2 else prog[i + 2])) else 0
                i += 4
    if pout[len(pout) - 1] > m:
        m = pout[len(pout) - 1]
print(m)
