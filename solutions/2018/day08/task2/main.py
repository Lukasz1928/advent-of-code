from treelib import Tree


def read_input():
    with open('input', 'r') as f:
        return [int(x) for x in f.read().split()]


def parse(gd, tree, parents, parent_id=None):
    children_count = gd[0]
    metadata_count = gd[1]
    current_id = len(parents)
    parents.add(current_id)
    if parent_id is not None:
        tree.create_node(str(current_id), str(current_id), parent=str(parent_id))
    else:
        tree.create_node(str(current_id), str(current_id))
    s = 2
    for _ in range(children_count):
        s += parse(gd[s:], tree, parents, current_id)
    metadata = gd[s:s + metadata_count]
    tree.get_node(str(current_id)).data = metadata
    return s + metadata_count


def build_tree(gd):
    tree = Tree()
    parents = set()
    parse(gd, tree, parents)
    return tree


def value_of(tree, node):
    node_children = tree.children(node)
    if len(node_children) == 0:
        return sum(tree.get_node(node).data)
    node_metadata = tree.get_node(node).data
    sorted_children = list(sorted(node_children, key=lambda n: int(n.tag)))
    return sum(value_of(tree, sorted_children[child_idx - 1].tag) for child_idx in node_metadata if 1 <= child_idx <= len(node_children))


graph_description = read_input()
tree = build_tree(graph_description)
root_value = value_of(tree, str(0))
print(root_value)

