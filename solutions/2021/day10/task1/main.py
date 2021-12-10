
def read_input():
    with open('input', 'r') as f:
        return [line.strip() for line in f.readlines()]


def find_first_invalid(s):
    while len(new := s.replace('()', '').replace('[]', '').replace('<>', '').replace('{}', '')) != len(s):
        s = new
    if len(s) == 0:
        return None
    chars = ')]>}'
    if any(c in s for c in chars):
        return s[min(s.find(c) for c in chars if c in s)]
    return None


lines = read_input()
pts = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0}
for l in lines:
    invalid = find_first_invalid(l)
score = sum([pts[find_first_invalid(line)] for line in lines])
print(score)
