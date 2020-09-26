

def read_input():
    ranges = []
    with open('input', 'r') as f:
        for l in f:
            low, high = l.split('-')
            ranges.append((int(low), int(high)))
    return ranges


ranges = read_input()
sranges = list(sorted(ranges, key=lambda x: (x[0], x[1])))
i = 0
low = 0
high = 0
while i < len(sranges):
    current_low = sranges[i][0]
    current_high = sranges[i][1]
    if high + 1 >= current_low:
        high = max(high, current_high)
    else:
        break
    i += 1

result = high + 1
print(result)
