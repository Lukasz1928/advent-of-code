import re
from numpy import argmin


def read_input():
    r = []
    with open('input', 'r') as f:
        for l in f:
            pattern = "p=<(-?\\d+),(-?\\d+),(-?\\d+)>, v=<(-?\\d+),(-?\\d+),(-?\\d+)>, a=<(-?\\d+),(-?\\d+),(-?\\d+)>"
            m = re.match(pattern, l.strip())
            r.append(((int(m.group(1)), int(m.group(2)), int(m.group(3))),
                      (int(m.group(4)), int(m.group(5)), int(m.group(6))),
                      (int(m.group(7)), int(m.group(8)), int(m.group(9)))))
    return r


p = read_input()
acc_sum = [sum([abs(x) for x in part[2]]) for part in p]

closest_zero = argmin(acc_sum)
print(closest_zero)
