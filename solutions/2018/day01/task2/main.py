
with open('input', 'r') as f:
    data = [l.strip() for l in f]

dfs = [int(x) for x in data]

freq = 0
freqs = {0}
found = False
while not found:
    for df in dfs:
        freq += df
        if freq in freqs:
            found = True
            break
        freqs.add(freq)

print(freq)
