from typing import List

from test_framework import generic_test

import heapq
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    # return []
    result=[]
    min_heap=[(l[0],i,0) for i,l in enumerate(sorted_arrays)]
    heapq.heapify(min_heap)
    while min_heap:
        smallest_index, curr = min_heap[0][1:]
        if curr+1<len(sorted_arrays[smallest_index]):
            pop=heapq.heapreplace(min_heap,(sorted_arrays[smallest_index][curr+1], smallest_index, curr+1))
            result.append(pop[0])
        else:
            result.append(heapq.heappop(min_heap)[0])
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
