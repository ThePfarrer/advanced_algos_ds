from heapq import heappop, heappush


def top_k(A, k):
    heap = []
    for el in A:
        if len(heap) == k and heap[0] < el:
            heappop(heap)
        if len(heap) < k:
            heappush(heap, el)
    return heap


