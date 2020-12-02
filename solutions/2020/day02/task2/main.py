import re


class Password:
    def __init__(self, line):
        m = re.match(r'(?P<low>\d+)-(?P<high>\d+) (?P<letter>\w): (?P<password>\w+)', line)
        self.letter = m.group('letter')
        self.password = m.group('password')
        self.bounds = int(m.group('low')), int(m.group('high'))

    def is_valid(self):
        return (self.password[self.bounds[0] - 1] == self.letter) != (self.password[self.bounds[1] - 1] == self.letter)


def read_input():
    with open('input', 'r') as f:
        lines = [Password(line.strip()) for line in f]
    return lines


passwords = read_input()
result = len([password for password in passwords if password.is_valid()])
print(result)
