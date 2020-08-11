import ast
import re


def read_input():
    with open('input', 'r') as f:
        return f.read().strip()


def remove_garbage(d):
    in_garbage = False
    d = d.replace("!!", "")
    clean_d = ""
    i = 0
    while i < len(d):
        if in_garbage:
            if d[i] == '>' and d[i - 1] != '!':
                in_garbage = False
            if i + 1 < len(d) and d[i + 1] == ',':
                i += 1
            i += 1
        else:
            if d[i] == '<':
                in_garbage = True
            else:
                clean_d += d[i]
            i += 1
    return re.sub(',+', ',', clean_d).replace('{,}', '{}')


def calculate_score(d, base_score=1):
    if len(d) == 0:
        return base_score
    score = base_score
    for g in d:
        score += calculate_score(g, base_score + 1)
    return score


raw_data = read_input()
clean_data = remove_garbage(raw_data)
data_as_lists = clean_data.replace('{', '[').replace('}', ']')
data = ast.literal_eval(data_as_lists)
score = calculate_score(data)
print(score)
