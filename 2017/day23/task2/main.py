# Original code seems impossible to run in a finite amount of time.
# It is supposed to count non-prime numbers in the range [b, c] with a step of 17(so {b, b+17, b+34,..., c}) are checked
# Basic idea of the original algorithm is described below:

# b = 106700
# c = 123700
# d = 0
# e = 0
# f = 0
# g = 0
# h = 0
# for b in range(low, high + 1, 17):  # iterate over all candidate numbers
#     f = 1  # flag - f = 1 for prime numbers
#     d = 2  # first potential divisor of b
#     while True:  # iterate over all possible divisors d in {2, 3,...,b}
#         e = 2  # second potential divisor of b
#         while True:  # iterate over all possible divisors e in {2, 3,...,b}
#             g = d * e - b  # check if b = d * e
#             e = e + 1
#             if g == 0:  # if b = d * e then b is composite
#                 f = 0
#             g = e - b  # end iteration if e = b because no bigger divisors are possible
#             if g == 0:
#                 break
#         d = d + 1
#         g = d - b  # end iteration if d = b because no bigger divisors are possible
#         if g == 0:
#             break
#     if f == 0:  # increase counter of composite numbers if b is composite
#         h = h + 1
#     g = b - high  # end iteration if b exceeds upper bound of interval
#     if g == 0:
#         break
#
# result = h
# print(result)


from math import sqrt, ceil


def is_prime(n):
    if n % 2 == 0:
        return False
    for d in range(3, ceil(sqrt(n)), 2):
        if n % d == 0:
            return False
    return True


low = 106700
high = 123700

cnt = 0
for b in range(low, high + 1, 17):
    if not is_prime(b):
        cnt += 1
print(cnt)

