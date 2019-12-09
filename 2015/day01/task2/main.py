d = open('input').read()
lvl = 0
res = None
for i, x in enumerate(d):
    lvl += (1 if x == '(' else -1)
    if lvl == -1:
        res = i + 1
        break
print(res)