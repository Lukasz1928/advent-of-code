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


def calculate_total_bag_contents(color, content):
    todo = [(color, 1)]
    total = 0
    while todo:
        name, count = todo.pop()
        todo.extend([(n, c * count) for n, c in content[name].items()])
        total += count
    return total - 1


bag_content, color_parent = read_input()
total_content = calculate_total_bag_contents('shiny gold', bag_content)
print(total_content)
