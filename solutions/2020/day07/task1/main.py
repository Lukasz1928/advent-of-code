import re


def parse_line(line):
    m = re.match('(?P<color>.*) bags contain (?P<content>.*)', line)
    bag_color = m.group('color')
    content = m.group('content')
    contents = re.findall(r'(?P<count>\d+) (?P<bag_name>[\w\s]*) bags?', content)
    return bag_color, {b[1]: int(b[0]) for b in contents}


def read_input():
    with open('input', 'r') as f:
        lines = [parse_line(line) for line in f]
    contents = {bag[0]: bag[1] for bag in lines}
    parents = {content_color: set() for content_color in contents.keys()}
    for bag in lines:
        for cont in bag[1]:
            parents[cont].add(bag[0])
    return contents, parents


def find_all_parents(color, parents):
    color_parents = set()
    todo = [color]
    while todo:
        current = todo.pop()
        if current in color_parents:
            continue
        color_parents.add(current)
        todo.extend([par for par in parents[current] if par not in color_parents])
    return color_parents - {color}


bag_content, color_parent = read_input()
shiny_gold_parents = find_all_parents('shiny gold', color_parent)
result = len(shiny_gold_parents)
print(result)
