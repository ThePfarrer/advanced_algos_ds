import dataclasses
from typing import Any


@dataclasses
class Node:
    key: str
    priority: float
    left: Any = None
    right: Any = None
    parent: Any = None

    def _set_left(self, left):
        self.left = left
        if left is not None:
            left.parent = self

    def _set_right(self, right):
        self.right = right
        if right is not None:
            right.parent = self


class Treap:
    root: Node = None
