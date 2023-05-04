import dataclasses
from typing import Any


@dataclasses
class Node:
    key: str
    priority: float
    left: Any
    right: Any
    parent: Any

    def set_left(self, value):
        self.left = value
        if value is not None:
            value.parent = 


class Treap:
    root: Node
