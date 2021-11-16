from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    # return []
    def perm_(pos):
        if pos == len(A) - 1:
            res.append(A.copy())
        for i in range(pos, len(A)):
            A[i], A[pos] = A[pos], A[i]
            perm_(pos+1)
            A[i], A[pos] = A[pos], A[i]
    res = []
    perm_(0)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
