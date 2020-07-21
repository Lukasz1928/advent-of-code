import numpy as np
import re

class Program:
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
		
	def __str__(self):
		return self.name + " (" + self.weight + ") " + str(self.children)
		
	
class Computer:
	def __init__(self):
		self.programs = []
		
	def add_program(self, program):
		self.programs.append(program)
		
	def _find_parent_of(self, program):
		pname = program if isinstance(program, str) else program.name
		for p in self.programs:
			if pname in p.children:
				return p.name
		return None
		
	def find_root(self):
		for p in self.programs:
			if self._find_parent_of(p) is None:
				return p.name
			
	def __str__(self):
		return str([str(p) for p in self.programs])
	

comp = Computer()
with open('input', 'r') as f:
	for line in f:
		m = re.match('(\w+) \((\d+)\)( -> (.*))?', line).groups()
		name, weight, children = m[0], m[1], [] if m[3] is None else m[3].split(', ')
		p = Program(name, weight, children)
		comp.add_program(p)
print(comp.find_root())