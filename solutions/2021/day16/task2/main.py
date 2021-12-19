from __future__ import annotations
from dataclasses import dataclass
from functools import reduce
from typing import Union, List, Tuple


def read_input():
    with open('input', 'r') as f:
        return f.read()


def to_bin(s: str) -> str:
    return ''.join([str(bin(int(x, 16)))[2:].zfill(4) for x in s])


def get_literal(s: str) -> Tuple[str, str]:
    groups = []
    while True:
        group = s[:5].rjust(5, '0')
        groups.append(group)
        s = s[5:]
        if group[0] == '0':
            break
    val = ''.join(grp[1:] for grp in groups)
    return val, s


@dataclass
class Packet:
    version: int
    type: int
    val: Union[int, List[Packet]]

    def value(self) -> int:
        if self.type == 0:
            return sum(v.value() for v in self.val)
        if self.type == 1:
            return reduce(lambda agg, v: agg * v.value(), self.val, 1)
        if self.type == 2:
            return min([v.value() for v in self.val])
        if self.type == 3:
            return max([v.value() for v in self.val])
        if self.type == 4:
            return self.val
        if self.type == 5:
            return int(self.val[0].value() > self.val[1].value())
        if self.type == 6:
            return int(self.val[0].value() < self.val[1].value())
        if self.type == 7:
            return int(self.val[0].value() == self.val[1].value())

    @staticmethod
    def from_str(s: str, max_count: int = None) -> Tuple[List[Packet], str]:
        packets = []
        while s != "" and '1' in s:
            ver = int(s[:3], 2)
            tp = int(s[3:6], 2)
            if tp == 4:
                x, s = get_literal(s[6:])
                packets.append(Packet(version=ver, type=tp, val=int(x, 2)))
            else:
                if s[6] == '0':
                    l = int(s[7:22], 2)
                    nested, _ = Packet.from_str(s[22:22 + l])
                    s = s[22 + l:]
                    packets.append(Packet(version=ver, type=tp, val=nested))
                else:
                    l = int(s[7:18], 2)
                    nested = []
                    for _ in range(l):
                        nest, s = Packet.from_str(s[18:], l - len(nested))
                        nested.extend(nest)
                        if len(nested) == l:
                            break
                    packets.append(Packet(version=ver, type=tp, val=nested))
            if len(packets) == max_count:
                break
        return packets, s


bin_data = to_bin(read_input())
packets, _ = Packet.from_str(bin_data)
result = packets[0].value()
print(result)
