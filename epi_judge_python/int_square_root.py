from test_framework import generic_test

import math
def square_root(k: int) -> int:
    # TODO - you fill in here.
    # return 0
    ##direct sol.
    #return math.floor(math.sqrt(k))
    lower, upper = 0, k
    root = None
    while lower <= upper:
        middle = (lower + upper) >> 1
        square=middle *middle
        if square> k:
            upper = middle - 1
        elif square == k:
            return middle
        elif square < k:
            lower = middle + 1
            root = middle
    return root

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
