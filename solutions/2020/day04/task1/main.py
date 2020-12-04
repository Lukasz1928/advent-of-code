import re


def parse_passport(passport):
    pairs = re.sub(r'\s+', ' ', passport).split()
    return dict(p.split(':') for p in pairs)


def read_input():
    with open('input', 'r') as f:
        raw_text = f.read()
    return [parse_passport(p) for p in raw_text.split('\n\n')]


def is_valid(passport):
    return len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport.keys())


passports = read_input()

valid_passports_count = len([p for p in passports if is_valid(p)])
print(valid_passports_count)
