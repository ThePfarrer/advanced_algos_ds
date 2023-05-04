import collections
from dataclasses import dataclass, field
from typing import Any

from heap.heap import Heap, Pair


@dataclass(order=True)
class TreeNode:
    sort_index: int = field(init=False, repr=False)
    chars: str
    freq: int
    left: Any = None
    right: Any = None

    def __post_init__(self):
        self.sort_index = self.freq


def huffman(text: str, branching_factor: int):
    # char_frequencie_map = compute_frequencies(text)
    # priority_queue = []

    return build_table(heap_to_tree(freq_to_heap(compute_frequencies(text), branching_factor)), "", {})


def build_table(node, sequence, chars_to_sequence_map):
    if len(node.chars) == 1:
        chars_to_sequence_map[node.chars[0]] = sequence
    else:
        if node.left is not None:
            build_table(node.left, sequence + "0", chars_to_sequence_map)
        if node.right is not None:
            build_table(node.right, sequence + "1", chars_to_sequence_map)

    return chars_to_sequence_map


def compute_frequencies(txt):
    return collections.Counter(txt)


def freq_to_heap(freq_map, branching_factor=2):
    heap = []
    for ch, freq in freq_map.items():
        heap.append(Pair(TreeNode(str(ch), freq), freq))

    return Heap(heap, branching_factor)


def heap_to_tree(heap):
    while len(heap) > 1:
        right = heap.top()
        left = heap.top()

        parent = TreeNode(left.chars + right.chars, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heap.insert(parent, parent.freq)

    return heap.top()
