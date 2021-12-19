from __future__ import annotations
from ast import literal_eval
from typing import Union, Optional


class Number:
    def __init__(self, parent: Optional[Number]):
        self.left = None
        self.right = None
        self.parent = parent

    def initialise(self, left: Union[Number, int], right: Union[Number, int]):
        self.left = left
        self.right = right
        return self

    @staticmethod
    def from_list(data: list, parent: Optional[Number] = None) -> Number:
        l, r = data
        n = Number(parent)
        if not isinstance(l, int):
            l = Number.from_list(l, n)
        if not isinstance(r, int):
            r = Number.from_list(r, n)
        return n.initialise(l, r)

    def _should_explode(self) -> bool:
        parents = 0
        current = self
        while current is not None and parents < 4:
            current = current.parent
            parents += 1
        return parents >= 4

    def reduce(self) -> Number:


    def __add__(self, other: Number) -> Number:
        n = Number(parent=None).initialise(self, other)
        return n.reduce()


def read_input():
    with open('input', 'r') as f:
        lines = [l for l in f]
    lists = [literal_eval(l) for l in lines]
    return [Number.from_list(d) for d in lists]


numbers = read_input()
print(numbers)