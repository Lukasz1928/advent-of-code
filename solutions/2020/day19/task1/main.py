# That's probably not the fastest solution in existence :)


def read_input():
    with open('input', 'r') as f:
        rs, msgs = f.read().split('\n\n')
    prods = []
    for r in rs.split('\n'):
        left, right = r.split(': ')
        r = [tuple(tok if tok.isnumeric() else tok[1:-1] for tok in g.split()) for g in right.split(' | ')]
        for prod in r:
            p = Production(left, prod)
            prods.append(p)
    return prods, msgs.split('\n')


def find_terminals(prods):
    terms = set()
    for p in prods:
        for char in p.right:
            if not char.isnumeric():
                terms.add(char)
    return terms


class Production:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_terminal(self):
        return all(not x.isnumeric() for x in self.right)

    @property
    def id(self):
        return int(self.left)

    def __str__(self):
        return f'{self.left} -> {self.right}'


def to_cnf(prods):
    # eliminate productions with more than 2 nonterminals on the RHS
    replaced_idx = 1000
    prods2 = []
    for prod in prods:
        if len(prod.right) > 2:
            p = Production(prod.left, (prod.right[0], replaced_idx + 1))
            prods2.append(p)
            rest = prod.right[1:]
            replaced_idx += 1
            while len(rest) > 2:
                p = Production(str(replaced_idx), (rest[0], replaced_idx + 1))
                prods2.append(p)
                rest = rest[1:]
                replaced_idx += 1
            p = Production(str(replaced_idx), rest)
            prods2.append(p)
        else:
            prods2.append(prod)
    # eliminate unit rules
    prods3 = []
    for prod in prods2:
        if len(prod.right) == 1 and not prod.is_terminal():
            for cprod in prods2:
                if prod.right[0] == cprod.left:
                    p = Production(prod.left, cprod.right)
                    prods3.append(p)
        else:
            prods3.append(prod)
    return prods3


def word_in_grammar(prods, word):
    n = len(word)
    word = " " + word
    P = [[{k: False for k in [p.id for p in prods]} for _ in range(n + 1)] for _ in range(n + 1)]
    for s in range(1, n + 1):
        for prod in [p for p in prods if p.right == (word[s],)]:
            P[1][s][prod.id] = True
    for l in range(2, n + 1):
        for s in range(1, n - l + 1 + 1):
            for p in range(1, l - 1 + 1):
                for prod in [p for p in prods if not p.is_terminal()]:
                    if P[p][s][int(prod.right[0])] and P[l - p][s + p][int(prod.right[1])]:
                        P[l][s][int(prod.left)] = True
    return P[n][1][0]


productions, messages = read_input()
cnf_productions = to_cnf(productions)
result = len([msg for msg in messages if word_in_grammar(cnf_productions, msg)])
print(result)
