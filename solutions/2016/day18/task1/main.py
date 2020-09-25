

def read_input():
    with open('input', 'r') as f:
        return f.read().strip()


def is_save(ngh):
    return tuple(ngh) not in {('^', '^', '.'), ('.', '^', '^'), ('^', '.', '.'), ('.', '.', '^')}


def next_row(p):
    temp = '.' + p + '.'
    res = ""
    for i in range(len(p)):
        res += '.' if is_save(temp[i:i + 3]) else '^'
    return res


pat = read_input()
cnt = pat.count('.')
for _ in range(39):
    pat = next_row(pat)
    cnt += pat.count('.')
print(cnt)
