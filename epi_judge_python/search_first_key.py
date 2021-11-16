from typing import List

from test_framework import generic_test

import bisect
def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    # # return 0
    #apply bisect module
    # i=bisect.bisect_left(A,k)
    # if i in range(0,len(A)) and A[i]==k:
    #     return i
    # else:
    #     return -1

    #naive approach
    recent_k = -1
    lower, upper = 0, len(A) - 1
    while lower <= upper:
        middle = (lower + upper) >> 1
        # if lower == upper:
        #     if A[middle] == k:
        #         recent_k = middle
        #     return recent_k
        if A[middle] == k:
            recent_k = middle
            upper = middle - 1
        elif A[middle] > k:
            upper = middle - 1
        elif A[middle] < k:
            lower = middle + 1
    return recent_k


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
