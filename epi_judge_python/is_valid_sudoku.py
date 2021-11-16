from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    # import math
    # n = len(partial_assignment)
    # for i in range(n):
    #     _row_digits = list(range(n + 1))
    #     _col_digits = list(range(n + 1))
    #     for j in range(n):
    #         if _row_digits[partial_assignment[i][j]] == -1:
    #             return False
    #         elif _row_digits[partial_assignment[i][j]] == 0:
    #             pass
    #         else:
    #             _row_digits[partial_assignment[i][j]] = -1
    #
    #         if _col_digits[partial_assignment[j][i]] == -1:
    #             return False
    #         elif _col_digits[partial_assignment[j][i]] == 0:
    #             pass
    #         else:
    #             _col_digits[partial_assignment[j][i]] = -1
    #
    # small_n = int(math.sqrt(n))
    # for i in range(0, n, small_n):
    #     for j in range(0, n, small_n):
    #         _n_digits = list(range(n + 1))
    #         for k in range(small_n):
    #             for l in range(small_n):
    #                 if _n_digits[partial_assignment[i + k][j + l]] == -1:
    #                     return False
    #                 elif _n_digits[partial_assignment[i + k][j + l]] == 0:
    #                     pass
    #                 else:
    #                     _n_digits[partial_assignment[i + k][j + l]] = -1
    # return True

    import math
    import collections
    length = len(partial_assignment)
    region = int(math.sqrt(length))
    return max(
        collections.Counter(
            k for i,row in enumerate(partial_assignment)
                for j,n in enumerate(row) if n!=0
                for k in ((i,str(n)), (str(n),j), (i//region, j//region, str(n)))
        ).values(),default=0
    ) <=1




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
