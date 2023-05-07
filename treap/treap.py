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

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_root(self):
        return self.parent is None

    def is_left_child(self):
        return

    def search(self, key, priority):
        pass

    def add(self, key, priority):
        pass

    def _left_rotate(self):
        if self.is_root():
            return
        parent = self.parent
        self.parent = parent.parent if parent is not None else None
        if parent is not None:
            parent._set_right(self.left)
        self._set_left(parent)
        return self

    def _right_rotate(self):
        if self.is_root():
            return
        parent = self.parent
        self.parent = parent.parent if parent is not None else None
        if parent is not None:
            parent._set_left(self.right)
        self._set_right(parent)
        return self

    # def right_rotate(self):
    #     if self.is_root():
    #         raise ValueError("Right rotate called on root")
    #     # parent = self.get_parent()
    #     parent = self.parent
    #     # self.parent = parent.get_parent() if parent is not None else None
    #     self.parent = parent.parent if parent is not None else None
    #     if parent is not None:
    #         parent._set_left(self.right)
    #     self._set_right(parent)
    #     return self


class Treap:
    root: Node = None
