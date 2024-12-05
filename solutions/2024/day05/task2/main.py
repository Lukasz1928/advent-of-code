from collections import defaultdict


def read_input() -> tuple[set[tuple[int, int]], list[list[int]]]:
    with open('input', 'r') as f:
        content = f.read()

    rules_section, pages_section = content.split('\n\n')

    rules = set()
    for line in rules_section.split('\n'):
        l, r = line.split('|')
        rules.add((int(l), int(r)))

    pages = []
    for line in pages_section.split('\n'):
        pages.append([int(p) for p in line.split(',')])

    return rules, pages


def get_ordered(rules: set[tuple[int, int]], numbers: list[int]) -> list[int]:
    after = {num: set() for num in numbers}
    for rule in rules:
        if rule[0] in numbers and rule[1] in numbers:
            after[rule[0]].add(rule[1])

    after_len = {l: len([item for item in r if item in numbers]) for l, r in after.items()}

    return [item[0] for item in sorted(after_len.items(), key=lambda it: it[1], reverse=True)]


def is_valid(rules: set[tuple[int, int]], order: list[int]):
    for left_idx, left_page in enumerate(order[:-1]):
        for right_idx, right_page in enumerate(order[left_idx+1:]):
            if (right_page, left_page) in rules:
                return False
    return True


rules, pages = read_input()
nums = {num for r in rules for num in r}

result = 0

for pages_order in pages:
    if not is_valid(rules, pages_order):
        ordered = get_ordered(rules, pages_order)
        result += ordered[len(ordered) // 2]

print(result)
