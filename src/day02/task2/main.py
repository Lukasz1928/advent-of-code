for noun in range(0, 100):
    for verb in range(0, 100):
        prog = [int(x) for x in open('input', 'r').read().split(',')]
        prog[1] = noun
        prog[2] = verb
        for i in range(0, len(prog) - 3, 4):
            if prog[i] == 99:
                break
            prog[prog[i + 3]] = (prog[prog[i + 1]] + prog[prog[i + 2]]) if prog[i] == 1 else (prog[prog[i + 1]] * prog[prog[i + 2]])
        if prog[0] == 19690720:
            print(100 * noun + verb)
            exit()
