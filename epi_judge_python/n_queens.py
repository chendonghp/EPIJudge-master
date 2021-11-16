from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    # return []
    def n_queen(row):
        if row == n:
            result.append(col_placement.copy())
            return
        for col in range(n):
            # not in the same col, not in the diagonal
            if all(
                abs(col - c) not in (0, row-i)
                for i, c in enumerate(col_placement[:row])
            ):
                col_placement[row] = col
                n_queen(row+1)
    result = []
    col_placement = [0]*n
    n_queen(0)
    return result

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
