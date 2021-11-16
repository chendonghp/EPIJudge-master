from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.
    # return 0
    lower,upper=0,len(A)-1
    while lower<=upper:
        middle=(upper+lower)>>1
        if A[middle]>A[upper]:
            lower=middle+1
        elif A[middle]<A[upper]:
            upper=middle
    return lower


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
