import hashlib

with open('input', 'r') as f:
    door_id = f.read()

pl = 8
chars = [None] * pl
i = 0
while len([x for x in chars if x is not None]) < pl:
    while True:
        h = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        i += 1
        if h.startswith("00000") and 0 <= int(h[5], 16) <= 7 and chars[int(h[5])] is None:
            chars[int(h[5])] = h[6]
            print(h[5] + " -> " + h[6])
            break
password = "".join(chars)
print(password)
