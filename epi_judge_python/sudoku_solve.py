
import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    # return

    def satisfied_num(i, j):
        nums = list(range(1, 10))
        for k in range(9):
            val = partial_assignment[i][k]
            if val and val in nums:
                nums.remove(val)
        for k in range(9):
            val = partial_assignment[k][j]
            if val and val in nums:
                nums.remove(val)
        base_r, base_c = i//3 , j//3
        for r in range(3):
            for c in range(3):
                val = partial_assignment[base_r*3+r][base_c*3+c]
                if val and val in nums:
                    nums.remove(val)
        return nums

    def next_pos(i, j):
        if j == 8:
            i += 1
            j = 0
        else:
            j += 1
        return i, j

    def start_index(partial_assignment):
        i, j = 0, 0
        while partial_assignment[i][j] != 0:
            if j == 8:
                i += 1
                j = 0
            else:
                j += 1
        return i, j

    def backtracking(i, j):
        find = False
        if i == 9 and j == 0:
            find = True
            return find
        if partial_assignment[i][j] == 0:
            s = satisfied_num(i, j)
            for e in s:
                partial_assignment[i][j] = e
                new_i, new_j = next_pos(i, j)
                find = backtracking(new_i, new_j)
                if find:
                    break
                partial_assignment[i][j] = 0
        else:
            new_i, new_j = next_pos(i, j)
            find = backtracking(new_i, new_j)
        return find
    start_i, start_j = start_index(partial_assignment)
    return backtracking(start_i, start_j)



def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
