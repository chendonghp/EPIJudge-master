from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    # return True
    # check each loacation if there is a bridge over it.
    # for p in range(1,len(A)):
    #     for i in range(p):
    #         if i+A[i]>=p:
    #             break
    #         if i==p-1:
    #             return False
    # return True
    furthest=0
    for p in range(len(A)-1):
        if p+A[p]>furthest:
            furthest=p+A[p]
        if p==furthest:
            return False
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
