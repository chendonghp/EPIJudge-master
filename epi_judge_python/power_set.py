from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    # return []
    def power(pos):
        # not len(input_set) - 1
        if pos == len(input_set):
            res.append(sub_set.copy())
            return
        for i in range(2):
            if i == 1:
                sub_set.append(input_set[pos])
            power(pos+1)
            # restore state
            if i == 1:
                sub_set.remove(input_set[pos])
    res = []
    sub_set = []
    power(0)
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
