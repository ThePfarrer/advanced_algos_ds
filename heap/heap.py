from dataclasses import dataclass
from typing import Any


@dataclass
class Pair:
    element: Any
    priority: int


class Heap:
    def __init__(self, pairs=[], branches=2):
        self.pairs = pairs
        self.branches = branches
        # self.hash_map = {}

        if not self.is_empty():
            self._heapify()

    def __len__(self):
        """Size of the heap.

        Returns: The number of elements in the heap.
        """
        return len(self.pairs)

    def print(self):
        return self.pairs, len(self)

    def is_empty(self):
        return len(self.pairs) == 0

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Method peek called on an empty heap.")
        return self.pairs[0].element

    def top(self):
        if self.is_empty():
            raise RuntimeError("Method peek called on an empty heap.")
        p = self.pairs.pop()
        if not self.pairs:
            return p.element
        else:
            element = self.pairs[0].element
            self.pairs[0] = p
            self._push_down(self.pairs)
            return element

    def insert(self, element, priority):
        p = Pair(element, priority)
        self.pairs.append(p)
        self._bubble_up(self.pairs, len(self.pairs) - 1)

    def remove(self, element):
        index = self.tuple_index(element, self.pairs)
        self.pairs[index] = self.pairs[-1]
        self.pairs.pop()

        parent_index = self._get_parent_index(index, self.branches)

        if self.pairs[parent_index].priority > self.pairs[index].priority:
            self._bubble_up(self.pairs, index)
        elif self.pairs[parent_index].priority < self.pairs[index].priority:
            self._push_down(self.pairs, index)

    def update(self, element, new_priority):
        index = self.tuple_index(element, self.pairs)
        if index >= 0:
            old_priority = self.pairs[index].priority
            self.pairs[index] = Pair(element, new_priority)
            if old_priority > new_priority:
                self._bubble_up(self.pairs, index)
            elif old_priority < new_priority:
                self._push_down(self.pairs, index)

    def _bubble_up(self, pairs, index):
        current = pairs[index]
        while index > 0:
            parent_index = self._get_parent_index(index)
            if pairs[parent_index].priority > current.priority:
                pairs[index] = pairs[parent_index]
                # self.hash_map[pairs[index].element] = index
                index = parent_index
            else:
                break
        pairs[index] = current
        # self.hash_map[pairs[index].element] = index

    def _push_down(self, pairs, index=0):
        current = pairs[index]
        while index < self._first_leaf_index(pairs):
            (child, child_index) = self._highest_priority_child(index)
            if child.priority < current.priority:
                pairs[index] = pairs[child_index]
                # self.hash_map[pairs[index].element] = index
                index = child_index
            else:
                break
        pairs[index] = current
        # self.hash_map[pairs[index].element] = index

    # def contains(self, elem):
    #     index = self.hash_map.get(elem, -1)
    #     return index >= 0

    # def tuple_index(self, element, pairs):
    #     for ind, el in enumerate(pairs):
    #         if el.element == element:
    #             return ind
    #
    #     raise IndexError("Element not in array.")

    def _get_parent_index(self, index):
        return int((index - 1) / self.branches)

    def _first_leaf_index(self, pairs):
        return (len(pairs) - 2) // self.branches + 1

    def _highest_priority_child(self, index):
        child_indx = []
        for i in range(1, self.branches + 1):
            indx = self.branches * index + i
            if indx < len(self.pairs):
                child_indx.append(indx)

        highest_priority = child_indx[0]

        for ind in child_indx[1:]:
            if self.pairs[ind].priority < self.pairs[highest_priority].priority:
                highest_priority = ind

        return self.pairs[highest_priority], highest_priority

    def _heapify(self):
        last_inner_node_index = self._first_leaf_index(self.pairs) - 1
        for index in range(last_inner_node_index, -1, -1):
            self._push_down(self.pairs, index)

    
