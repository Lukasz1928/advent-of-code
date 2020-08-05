from collections import Counter

with open('input', 'r') as f:
    msgs = [l.strip() for l in f]

msg = ""
for i in range(len(msgs[0])):

    c = Counter([m[i] for m in msgs])
    mc = c.most_common()
    lc = mc[len(mc) - 1][0]
    msg += lc
print(msg)
