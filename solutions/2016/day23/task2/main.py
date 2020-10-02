# trying to run the given code has no chance of finishing any time soon
# the task is to calculate 12! + 81 * 91
# the assembuny code calculates x * y by adding 1 to a variable x * y in two nested loops


a = 12
c = 85
d = 91

result = 1
for mult in range(1, a + 1):
    result *= mult
result += c * d
print(result)
