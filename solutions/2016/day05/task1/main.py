import hashlib

with open('input', 'r') as f:
    door_id = f.read()

password = ""
i = 0
for _ in range(8):
    while True:
        h = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        i += 1
        if h.startswith("00000"):
            password += h[5]
            break
print(password)
