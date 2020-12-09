
def read_input():
    with open('input', 'r') as f:
        return [int(line.strip()) for line in f]


def sums_to(numbers, sm):
    for ni, n in enumerate(numbers):
        for ki, k in enumerate(numbers[ni:]):
            if n + k == sm:
                return True
    return False


def find_number_without_sum(numbers, preamble_length):
    for idx, number in enumerate(numbers[preamble_length:], preamble_length):
        previous = numbers[idx - preamble_length:idx]
        if not sums_to(previous, number):
            return number


def find_numbers_with_sum(numbers, sm):
    i1, i2 = 0, 1
    while True:
        s = sum(numbers[i1:i2])
        if s == sm:
            return numbers[i1:i2]
        if s > sm:
            i1 += 1
        if s < sm:
            i2 += 1


numbers = read_input()
preamble_length = 25

number_without_sum = find_number_without_sum(numbers, preamble_length)

sum_range = find_numbers_with_sum(numbers, number_without_sum)

result = min(sum_range) + max(sum_range)
print(result)
