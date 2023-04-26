import collections
import heapq
from heap.heap import Heap, Pair
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class TreeNode:
    sort_index: int = field(init=False, repr=False)
    # element: str
    chars: str
    freq: int
    # priority: int
    left: Any = None
    right: Any = None

    def __post_init__(self):
        self.sort_index = self.freq
        # self.sort_index = self.priority


def huffman(text):
    # char_frequencie_map = compute_frequencies(text)
    # priority_queue = []

    # freq_to_heap(compute_frequencies(text), priority_queue)

    # heap_to_tree(freq_to_heap(compute_frequencies(text), priority_queue))

    return build_table(
        heap_to_tree(freq_to_heap(compute_frequencies(text))), "", {}
    )


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


def freq_to_heap(freq_map):
    heap = []
    for ch, freq in freq_map.items():
        heap.append(Pair(TreeNode(ch, freq), freq))
        # heapq.heappush(heap, TreeNode(ch, freq))

    return Heap(heap)
    # return heap


def heap_to_tree(heap):
    while len(heap) > 1:
        right = heap.top()
        # right = heapq.heappop(heap)
        left = heap.top()
        # left = heapq.heappop(heap)

        parent = TreeNode(left.chars + right.chars, left.freq + right.freq)
        # parent = TreeNode(left.element + right.element, left.priority + right.priority)
        parent.left = left
        parent.right = right
        # heapq.heappush(heap, parent)
        heap.insert(parent, parent.freq)

    # return heapq.heappop(heap)
    return heap.top()
