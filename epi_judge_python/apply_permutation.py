from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    # return
    # #brute-force
    # B=[None]*len(A)
    # for i,a in zip(perm,A):
    #     B[i]=a
    # for i in range(len(A)):
    #     A[i] = B[i]
    for i in range(len(A)):
        cyc_index=i
        # t=A[cyc_index]
        while perm[cyc_index]>0:
            A[i],A[perm[cyc_index]]=A[perm[cyc_index]],A[i]
            t=perm[cyc_index]
            perm[cyc_index]-=len(A)
            cyc_index = t



def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
