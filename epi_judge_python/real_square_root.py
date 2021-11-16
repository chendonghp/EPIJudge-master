from test_framework import generic_test
import math


def square_root(x: float) -> float:
    # TODO - you fill in here.
    # return 0.0
    if x > 0:
        lower, upper = (x, 1.) if x < 1. else (1., x)
        while not math.isclose(lower, upper):
            middle = (lower+upper) / 2
            square = middle*middle
            if square > x:
                upper = middle
            else:
                lower = middle
        return lower


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
