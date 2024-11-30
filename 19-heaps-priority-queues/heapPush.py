import heapq
from typing import List


def heap_push(heap: List[int], value: int) -> int:
    heapq.heappush(heap, value)
    return heap[0]
