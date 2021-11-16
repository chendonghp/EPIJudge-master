from typing import List

from test_framework import generic_test

import heapq
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    # return []
    increasing = True
    arrays = []
    end = 0
    i = 0
    while i < len(A) - 1:
        if increasing and A[i + 1] < A[i]:
            start = end
            end = i + 1
            arrays.append(A[start:end])
            increasing = False
        elif not increasing and A[i + 1] >= A[i]:
            start = end
            end = i + 1
            arrays.append(list(reversed(A[start:end])))
            increasing = True
        i += 1
    if increasing:
        arrays.append(A[end:])
    else:
        arrays.append(list(reversed(A[end:])))
    return list(heapq.merge(*arrays))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
