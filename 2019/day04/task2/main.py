low, high = (int(x) for x in open('input', 'r').read().split('-'))
print(sum([all(int(x) >= int(y) for ix, x in enumerate(str(p)) for iy, y in enumerate(str(p)) if ix > iy) and any(str(p)[i - 3] != str(p)[i - 2] == str(p)[i - 1] != str(p)[i] for i in range(len(str(p)))) for p in range(low, high)]))
