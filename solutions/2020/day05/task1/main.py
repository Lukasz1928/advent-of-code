print(max([8 * int(''.join(str(int(d == 'B')) for d in pas[:7]), 2) +
           int(''.join(str(int(d == 'R')) for d in pas[7:]), 2)
           for pas in [line.strip() for line in open('input', 'r')]]))
