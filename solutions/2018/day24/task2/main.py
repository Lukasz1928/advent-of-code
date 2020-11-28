import re
from copy import deepcopy


def parse_traits(traits):
    traits_list = traits[1:-2].split('; ')
    if traits_list == ['']:
        return set(), set()
    weaknesses = set()
    immunities = set()
    for t in traits_list:
        lst = t[10 if t.startswith('immune') else 8:].split(', ')
        if t.startswith('immune'):
            immunities = immunities.union(set(lst))
        else:
            weaknesses = weaknesses.union(set(lst))
    return weaknesses, immunities


class Group:
    def __init__(self, id, units, hp, dmg, dmg_type, initiative, weaknesses, immunities):
        self.id = id
        self.units = units
        self.hp = hp
        self.dmg = dmg
        self.dmg_type = dmg_type
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities

        self.target = None

    def __str__(self):
        return f'{self.id}, units={self.units}'

    def get_group(self):
        return self.id[:2]

    def __hash__(self):
        return hash(self.id)

    # create a group from description
    # eg. "5711 units each with 6662 hit points (immune to fire; weak to slashing) with an attack that does 9 bludgeoning damage at initiative 14"
    @staticmethod
    def from_string(text, name):
        pattern = (r'(?P<count>\d+) units each with (?P<hp>\d+) hit points (?P<traits>(?:\(.*\) )?)with an attack that '
                   r'does (?P<dmg>\d+) (?P<dmg_type>\w+) damage at initiative (?P<initiative>\d+)')
        match = re.match(pattern, text)
        units = int(match.group('count'))
        hp = int(match.group('hp'))
        traits_description = match.group('traits')
        dmg = int(match.group('dmg'))
        dmg_type = match.group('dmg_type')
        initiative = int(match.group('initiative'))
        weaknesses, immunities = parse_traits(traits_description)
        return Group(name, units, hp, dmg, dmg_type, initiative, weaknesses, immunities)

    def effective_power(self):
        return self.units * self.dmg

    def take_damage(self, dmg, dmg_type):
        real_dmg = self.damage_received(dmg, dmg_type)
        units_removed = min(real_dmg // self.hp, self.units)
        self.units = self.units - units_removed

    def damage_received(self, dmg, dmg_type):
        if dmg_type in self.immunities:
            return 0
        if dmg_type in self.weaknesses:
            return 2 * dmg
        return dmg

    def select_target(self, enemies):
        damages = [e.damage_received(self.effective_power(), self.dmg_type) for e in enemies]
        if len(damages) == 0:
            self.target = None
            return None
        max_dmg = max(damages)
        if max_dmg <= 0:
            self.target = None
            return None
        enemies_with_max_damage = [enemies[i] for i, d in enumerate(damages) if d == max_dmg and d > 0]

        effective_powers = [e.effective_power() for e in enemies_with_max_damage]
        max_effective_power = max(effective_powers)
        enemies_with_max_effective_power = [enemies_with_max_damage[i]
                                            for i, ep in enumerate(effective_powers) if ep == max_effective_power]

        initiatives = [e.initiative for e in enemies_with_max_effective_power]
        max_initiative = max(initiatives)
        enemies_with_max_initiative = [enemies_with_max_effective_power[i]
                                       for i, ini in enumerate(initiatives) if ini == max_initiative]
        self.target = enemies_with_max_initiative[0]
        return self.target

    def attack(self):
        if self.units <= 0 or self.target is None:
            return

        self.target.take_damage(self.effective_power(), self.dmg_type)


def read_input():
    with open('input', 'r') as f:
        text = f.read()
    imm, inf = text.split('\n\n')
    return [Group.from_string(i, f'IS{idx + 1}') for idx, i in enumerate(imm.split('\n')[1:])], \
           [Group.from_string(i, f'IN{idx + 1}') for idx, i in enumerate(inf.split('\n')[1:])]


def run_fight(imm_sys, infec, b):
    for im in imm_sys:
        im.dmg += b
    prev_units = -1
    while imm_sys and infec:
        all_groups_selection_phase = list(
            sorted(imm_sys + infec, key=lambda g: (g.effective_power(), g.initiative), reverse=True))
        selected_is = set()
        selected_in = set()
        for g in all_groups_selection_phase:
            if g.get_group() == 'IN':
                s = g.select_target([x for x in imm_sys if x not in selected_is])
                if s is not None:
                    selected_is.add(s)
            else:
                s = g.select_target([x for x in infec if x not in selected_in])
                if s is not None:
                    selected_in.add(s)
        all_groups_attack_phase = list(sorted(imm_sys + infec, key=lambda g: g.initiative, reverse=True))
        for g in all_groups_attack_phase:
            g.attack()
        imm_sys = [i for i in imm_sys if i.units > 0]
        infec = [i for i in infec if i.units > 0]
        current_units = sum(x.units for x in imm_sys) + sum(x.units for x in infec)
        if current_units == prev_units:
            return -1
        prev_units = current_units
    return sum(x.units for x in imm_sys) - sum(x.units for x in infec)


immune_system, infection = read_input()
boost = 0
while True:
    imm = deepcopy(immune_system)
    inf = deepcopy(infection)
    r = run_fight(imm, inf, boost)
    if r > 0:
        break
    boost += 1
print(r)
