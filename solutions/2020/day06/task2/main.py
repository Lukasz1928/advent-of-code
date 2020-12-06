import functools


def read_input():
    with open('input', 'r') as f:
        groups = f.read().split('\n\n')
    return [g.split('\n') for g in groups]


answers = read_input()

answer_sets = [[{ans for ans in person} for person in group] for group in answers]
common_answers = [functools.reduce(lambda acc, val: acc.intersection(val), ans) for ans in answer_sets]
count_sum = sum(len(s) for s in common_answers)
print(count_sum)
