import re
import numpy as np


class Rule:
    def __init__(self, s):
        m = re.match('(.*) => (.*)', s)
        self.left = tuple(tuple(1 if c == '#' else 0 for c in line) for line in m.group(1).split('/'))
        self.right = tuple(tuple(1 if c == '#' else 0 for c in line) for line in m.group(2).split('/'))
        self._matching_patterns = self._calculate_matching_patterns()

    def _calculate_matching_patterns(self):
        mps = set()
        mps.add(tuple(self.left))  # original pattern
        mps.add(tuple(reversed(self.left)))  # flipped vertically
        mps.add(tuple(tuple(reversed(x)) for x in self.left))  # flipped horizontally

        r90 = tuple(tuple(l) for l in np.rot90(self.left))  # rotated 90 degrees
        mps.add(r90)
        mps.add(tuple(reversed(r90)))
        mps.add(tuple(tuple(reversed(x)) for x in r90))

        r180 = tuple(tuple(l) for l in np.rot90(np.rot90(self.left)))  # rotated 180
        mps.add(r180)
        mps.add(tuple(reversed(r180)))
        mps.add(tuple(tuple(reversed(x)) for x in r180))

        r270 = tuple(tuple(l) for l in np.rot90(np.rot90(np.rot90(self.left))))  # rotated 270
        mps.add(r270)
        mps.add(tuple(reversed(r270)))
        mps.add(tuple(tuple(reversed(x)) for x in r270))

        return mps

    def matches(self, pat):
        return len(pat) == len(self.left) and tuple(tuple(p) for p in pat) in self._matching_patterns


def read_input():
    with open('input', 'r') as f:
        return [Rule(l) for l in f]


def process(pattern, rules):
    psize = len(pattern)
    result = []

    s = 2 if psize % 2 == 0 else 3
    groups = psize // 2 if s == 2 else psize // 3
    for gx in range(groups):
        result.extend([[], [], []] if s == 2 else [[], [], [], []])
        for gy in range(groups):
            grp = [x[s * gy:s * gy + s] for x in pattern[s * gx:s * gx + s]]
            for r in rules:
                if r.matches(grp):
                    rhs = r.right
                    for i in range(1, s + 2):
                        result[-i].extend(rhs[-i])
                    break
    return result


pattern = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
rules = read_input()

for _ in range(5):
    pattern = process(pattern, rules)

result = sum([sum(r) for r in pattern])
print(result)
