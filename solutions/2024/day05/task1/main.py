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


def is_valid(rules: set[tuple[int, int]], order: list[int]):
    for left_idx, left_page in enumerate(order[:-1]):
        for right_idx, right_page in enumerate(order[left_idx+1:]):
            if (right_page, left_page) in rules:
                return False
    return True


rules, pages = read_input()

result = sum(pages_order[len(pages_order) // 2] for pages_order in pages if is_valid(rules, pages_order))
print(result)
