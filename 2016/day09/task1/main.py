import re

with open('input', 'r') as f:
    file = f.read().strip()

decompressed = ""
while len(file) > 0:
    m = re.match(r"^\((\d+)x(\d+)\)", file)
    if m is None:
        decompressed += file[0]
        file = file[1:]
    else:
        l = int(m.group(1))
        reps = int(m.group(2))
        ml = len(m.group(0))
        to_decompress = file[ml:ml+l]
        decompressed += to_decompress * reps
        file = file[ml+l:]

result = len(decompressed)
print(result)
