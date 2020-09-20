import re


def read_input():
    with open('input', 'r') as f:
        t = f.read().strip()
    b = int(re.search('Generator B starts with (\\d+)', t).group(1))
    a = int(re.search('Generator A starts with (\\d+)', t).group(1))
    return a, b


class Generator:
    mod = 2147483647

    def __init__(self, start, mul, mulitple_of):
        self.value = start
        self.mul = mul
        self.multiple_of = mulitple_of

    def __iter__(self):
        return self

    def __next__(self):
        self.value = (self.value * self.mul) % Generator.mod
        while self.value % self.multiple_of != 0:
            self.value = (self.value * self.mul) % Generator.mod
        return self.value


def equal(a, b):
    sa = bin(a)[-16:].zfill(16)
    sb = bin(b)[-16:].zfill(16)
    return sa == sb


init_values = read_input()
gen_a = Generator(init_values[0], 16807, 4)
gen_b = Generator(init_values[1], 48271, 8)

tries = 5000000
matching_count = 0
for _ in range(tries):
    val_a = next(gen_a)
    val_b = next(gen_b)
    if equal(val_a, val_b):
        matching_count += 1
print(matching_count)
