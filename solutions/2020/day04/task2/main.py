import re


def parse_passport(passport):
    pairs = re.sub(r'\s+', ' ', passport).split()
    return dict(p.split(':') for p in pairs)


def read_input():
    with open('input', 'r') as f:
        raw_text = f.read()
    return [parse_passport(p) for p in raw_text.split('\n\n')]


def is_valid(passport):
    requirements = {
        'byr': lambda x: 2002 >= int(x) >= 1920,
        'iyr': lambda x: 2020 >= int(x) >= 2010,
        'eyr': lambda x: 2030 >= int(x) >= 2020,
        'hgt': lambda x: 193 >= int(x[:-2]) >= 150 if x.endswith('cm') else 76 >= int(x[:-2]) >= 59,
        'hcl': lambda x: x[0] == '#' and int(x[1:], 16) >= 0,
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: len(x) == 9 and int(x) >= 0
    }
    try:
        return all(req(passport[field]) for field, req in requirements.items())
    except Exception:
        return False


passports = read_input()

valid_passports_count = len([p for p in passports if is_valid(p)])
print(valid_passports_count)
