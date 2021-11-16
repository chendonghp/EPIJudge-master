from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    # return []
    A.reverse()
    i=0
    while True:
        if i==len(A):
            A.append(1)
            break
        if A[i]+1==10:
            A[i]=0
        else:
            A[i]+=1
            break
        i += 1
    return list(reversed(A))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
