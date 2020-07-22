import re


class Program:
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children_names = children

		self.children = None
		self.parent = None

	def insert_relatives(self, computer):
		self.children = []
		for c in self.children_names:
			self.children.append(computer.get_program(c))
		self.parent = computer.get_program(computer.find_parent_of(self.name))

	def get_level(self):
		n = self
		lvl = 0
		while n.parent is not None:
			n = n.parent
			lvl += 1
		return lvl

	def get_total_weight(self):
		if len(self.children) == 0:
			return self.weight
		return self.weight + sum([c.get_total_weight() for c in self.children])

	def is_balanced(self):
		if len(self.children) == 0:
			return True
		weights = [c.get_total_weight() for c in self.children]
		return len(set(weights)) == 1
		
	def __str__(self):
		return self.name + " (" + str(self.weight) + ") " + str(self.children_names)
		
	
class Computer:
	def __init__(self):
		self.programs = []
		
	def add_program(self, program):
		self.programs.append(program)

	def build_tree(self):
		for p in self.programs:
			p.insert_relatives(self)
		
	def find_parent_of(self, program):
		pname = program if isinstance(program, str) else program.name
		for p in self.programs:
			if pname in p.children_names:
				return p.name
		return None
		
	def find_root(self):
		for p in self.programs:
			if self.find_parent_of(p) is None:
				return p.name
				
	def get_leaves(self):
		l = []
		for p in self.programs:
			if len(p.children) == 0:
				l.append(p)
		return l
		
	def remove_program(self, program):
		self.programs.remove([p for p in self.programs if p.name == program][0])
				
	def get_program(self, name):
		a = [p for p in self.programs if p.name == name]
		if len(a) >= 1:
			return a[0]
		return None
			
	def __str__(self):
		return str([str(p) for p in self.programs])

	def find_correct_weight(self):
		nodes = [t[0] for t in sorted([(p, p.get_level()) for p in self.programs], key=lambda x: x[1], reverse=True)]
		unbalanced_nodes = [t for t in nodes if not t.is_balanced()]
		node_to_fix = unbalanced_nodes[0]
		node_to_fix_children_weights = [c.get_total_weight() for c in node_to_fix.children]
		children_weights_count = sorted([(w, c) for (w, c) in {w: node_to_fix_children_weights.count(w) for w in set(node_to_fix_children_weights)}.items()], key=lambda x: x[1], reverse=True)
		wrong_weight = children_weights_count[1][0]
		wrong_weight_child = [c for c in node_to_fix.children if c.get_total_weight() == wrong_weight][0]
		expected_weight = children_weights_count[0][0]
		dw = expected_weight - wrong_weight
		return wrong_weight_child.weight + dw


comp = Computer()
with open('input', 'r') as f:
	for line in f:
		m = re.match('(\w+) \((\d+)\)( -> (.*))?', line).groups()
		name, weight, children = m[0], int(m[1]), [] if m[3] is None else m[3].split(', ')
		p = Program(name, weight, children)
		comp.add_program(p)
comp.build_tree()

result = comp.find_correct_weight()
print(result)
