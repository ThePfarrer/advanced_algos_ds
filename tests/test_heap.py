import random

import pytest

from heap.heap import Pair, Heap

BRANCHING_FACTORS_TO_TEST = [2, 3, 4, 5, 6]


def test_heapify():
    for b in BRANCHING_FACTORS_TO_TEST:
        size = 4 + random.randint(0, 20)
        pairs = [
            Pair(ch, random.randint(0, 100)) for ch in range(ord("A"), ord("Z"))[:size]
        ]
        heap = Heap(pairs, b)

        assert size == len(heap)
        assert heap._validate()


def test_clear():
    for b in BRANCHING_FACTORS_TO_TEST:
        heap = Heap(branches=b)

        with pytest.raises(RuntimeError) as context:
            heap.peek()

        assert "Method peek called on an empty heap." in str(context.value)

        heap.insert("First", 1e14)

        assert "First" == heap.peek()

        heap.insert("b", 0)
        heap.insert("c", -0.99)
        heap.insert("Second", -1)
        heap.insert("a", 11)

        assert "Second" == heap.peek()


def test_insert_top():
    for b in BRANCHING_FACTORS_TO_TEST:
        heap = Heap(branches=b)

        with pytest.raises(RuntimeError) as context:
            heap.peek()

        assert "Method peek called on an empty heap." in str(context.value)

        heap.insert("First", 1e14)

        assert "First" == heap.top()
        assert heap.is_empty()

        heap.insert("b", 0)
        heap.insert("c", -0.99)
        heap.insert("Second", -1)
        heap.insert("a", 11)

        assert "Second" == heap.top()
        assert 3 == len(heap)

        for i in range(10):
            heap.insert(str(i), random.random())

        while not heap.is_empty():
            assert heap._validate()
            heap.top()
