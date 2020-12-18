import re


def read_input():
    with open('input', 'r') as f:
        return [l.strip().replace(' ', '') for l in f]


def next_token(expr):
    if expr[0].isnumeric():
        m = re.match(r'^(\d+).*', expr).group(1)
        return m, expr[len(m):]
    return expr[0], expr[1:]


def to_rpn(expr):
    expr = expr.strip().replace(' ', '')
    priority = {'+': 2, '*': 1}
    Q = []
    S = []
    while expr:
        token, expr = next_token(expr)
        if token.isnumeric():
            Q.append(token)
        elif token == '(':
            S.append('(')
        elif token == ')':
            while S:
                elem = S.pop()
                if elem == '(':
                    break
                Q.append(elem)
        else:
            while S and S[-1] != '(' and priority[S[-1]] >= priority[token]:
                Q.append(S.pop())
            S.append(token)
    while S:
        Q.append(S.pop())
    return Q


def evaluate(expr):
    rpn = to_rpn(expr)
    S = []
    for e in rpn:
        if e.isnumeric():
            S.append(int(e))
        else:
            if e == '*':
                S.append(S.pop() * S.pop())
            else:
                S.append(S.pop() + S.pop())
    return S[-1]


expressions = read_input()
result = sum(evaluate(exp) for exp in expressions)
print(result)
