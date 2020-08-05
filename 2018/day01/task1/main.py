
with open('input', 'r') as f:
    data = [l.strip() for l in f]

freq = sum(int(x) for x in data)
print(freq)

