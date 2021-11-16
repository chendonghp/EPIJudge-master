from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream: Iterator[int]) -> int:
    # TODO - you fill in here.
    # return 0
    import itertools
    def find_missing_element(stream: Iterator[int]) -> int:
        num = 1 << 16
        up16counter_ = [0] * num
        up_it, low_it = itertools.tee(stream)
        for ip in up_it:
            up16counter_[ip >> 16] += 1
        capacity = 1 << 16
        missing_up = next(i for i, _ in enumerate(up16counter_) if i < capacity)
        down16counter_ = [0] * num
        for ip in low_it:
            if (ip >> 16) == missing_up:
                down16counter_[((1 << 16) - 1) & ip] = 1
        for i, flag in enumerate(down16counter_):
            if flag == 0:
                return (missing_up << 16) | i
        raise ValueError('no missing value!')

def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
