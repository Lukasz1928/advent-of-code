
def read_input():
    with open('input', 'r') as f:
        groups = f.read().split('\n\n')
    return [g.split('\n') for g in groups]


answers = read_input()

answer_sets = [{ans for person in group for ans in person} for group in answers]
count_sum = sum(len(s) for s in answer_sets)
print(count_sum)
