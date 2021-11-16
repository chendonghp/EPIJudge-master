from typing import List

from test_framework import generic_test, test_utils

import heapq
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    # TODO - you fill in here.
    # return []
    if k<=0:
        return []
    max_heap=[(-A[0],0)]
    result=[]
    i=1
    while len(result)< k:
        item,index=heapq.heappop(max_heap)
        result.append(-item)
        if index*2+1 <len(A):
            heapq.heappush(max_heap,(-A[index*2+1],index*2+1))
        else:
            continue
        if index*2+2 <len(A):
            heapq.heappush(max_heap,(-A[index*2+2],index*2+2))
        else:
            continue
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
