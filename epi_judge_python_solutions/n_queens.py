from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            # 一定要调用copy方法, 不然后面修改col_placement的值会导致result的值也会变
            result.append(col_placement.copy())
            return
        for col in range(n):
            # Test if a newly placed queen will conflict any earlier queens placed before.
            if all(
                # c:以前占据的列, col:当前列, i:已经走了的row数, row:当前所在row
                # all([]) all 接受空列表也是True
                    abs(c - col) not in (0, row - i)
                    for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)
    result: List[List[int]] = []
    col_placement = [0] * n
    solve_n_queens(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
