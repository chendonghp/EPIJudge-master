import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    # TODO - you fill in here.
    min_, max_ = float('inf'), float('-inf')
    if not A:
        return None
    if len(A) == 1:
        return MinMax(A[0], A[0])
    if len(A) % 2 == 0:
        for i in range(0, len(A), 2):
            if A[i] < A[i+1]:
                max_ = max(A[i+1], max_)
                min_ = min(A[i], min_)
            else:
                max_ = max(A[i], max_)
                min_ = min(A[i + 1], min_)
    else:
        for i in range(0, len(A)-1, 2):
            if A[i] < A[i + 1]:
                max_ = max(A[i + 1], max_)
                min_ = min(A[i], min_)
            else:
                max_ = max(A[i], max_)
                min_ = min(A[i + 1], min_)
        if A[len(A)-1] > max_:
            max_ = A[len(A)-1]
        elif A[len(A)-1] < min_:
            min_ = A[len(A)-1]
    return MinMax(min_, max_)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
