from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.
    # return []
    for i in reversed(range(len(perm)-1)):
        if perm[i]<perm[i+1]:
            j=len(perm)-1
            while perm[j]<=perm[i]:
                j-=1
            perm[i],perm[j]=perm[j],perm[i]
            perm[i+1:]=reversed(perm[i+1:])
            break
        if i==0:
            return []
    if len(perm)==1:
        return []
    return perm

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
