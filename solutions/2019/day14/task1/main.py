from collections import defaultdict

import regex
import math


class Reaction:
    def __init__(self, required=None, produced=None):
        self.required_quantities = dict() if required is None else required
        self.produced_quantities = dict() if produced is None else produced

    @staticmethod
    def _parse_side(s):
        lst = s.split(',')
        result = {}
        for l in lst:
            value, name = regex.match(r'\s?(\d+) (\S+)', l)[1:3]
            result[name] = int(value)
        return result

    @staticmethod
    def from_string(s):
        sides = s.split(' => ')
        leftside = Reaction._parse_side(sides[0])
        rightside = Reaction._parse_side(sides[1])
        return Reaction(leftside, rightside)

    def produces(self, chem):
        return chem in self.produced_quantities.keys()


def previous(reactions, chem):
    return [r for r in reactions if r.produces(chem)][0]


def to_set(lst):
    d = defaultdict(lambda: 0)
    for l in lst:
        d[l[0]] += l[1]
    s = set()
    for k, v in d.items():
        s.add((k, v))
    return s


reactions = set([Reaction.from_string(l) for l in open('input', 'r').read().splitlines()])
required = {('FUEL', 1)}
leftovers = defaultdict(lambda: 0)
while len({x for x in required if x[0] != 'ORE'}) != 0:
    new_required = []
    for req in required:
        if req[0] != 'ORE':
            reaction = [r for r in reactions if r.produces(req[0])][0]
            required_chems = reaction.required_quantities
            produced_chems = reaction.produced_quantities

            if leftovers[req[0]] >= req[1]:
                leftovers[req[0]] -= req[1]
            else:
                required_reactions = math.ceil((req[1] - leftovers[req[0]]) / produced_chems[req[0]])
                for rn, rc in required_chems.items():
                    new_required.append((rn, required_reactions * rc))
                produced = required_reactions * produced_chems[req[0]]
                leftovers[list(produced_chems.keys())[0]] = produced - (req[1] - leftovers[req[0]])
        else:
            new_required.append(req)
    required = to_set(new_required)

ore_collected = 1000000000000
main_produced = ore_collected // list(required)[0][1]
leftover_produced = 0 # TODO