
def read_input():
    with open('input', 'r') as f:
        return [int(line.strip()) for line in f]


def sums_to(numbers, sm):
    for ni, n in enumerate(numbers):
        for ki, k in enumerate(numbers[ni:]):
            if n + k == sm:
                return True
    return False


numbers = read_input()
preamble_length = 25
result = None
for idx, number in enumerate(numbers[preamble_length:], preamble_length):
    previous = numbers[idx - preamble_length:idx]
    if not sums_to(previous, number):
        result = number
        break
print(result)
