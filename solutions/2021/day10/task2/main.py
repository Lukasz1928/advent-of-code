from functools import reduce


def read_input():
    with open('input', 'r') as f:
        return [line.strip() for line in f.readlines()]


def remove_pairs(s):
    while len(new := s.replace('()', '').replace('[]', '').replace('<>', '').replace('{}', '')) != len(s):
        s = new
    chars = ')]>}'
    if not any(c in s for c in chars):
        return s
    return ''


lines = read_input()
pts = {'(': 1, '[': 2, '{': 3, '<': 4, }
scores = [reduce(lambda agg, curr: agg * 5 + pts[curr], remove_pairs(line)[::-1], 0) for line in lines]
positive_scores = [s for s in scores if s > 0]
result = list(sorted(positive_scores))[len(positive_scores) // 2]
print(result)
