from typing import List

from test_framework import generic_test

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
import random


def find_kth_largest(k: int, A: List[int]) -> int:
    # TODO - you fill in here.
    # return 0
    # # naive: sorting
    # A.sort(reverse=True)
    # return A[k-1]

    def partition(pivot_idx, lower, upper):
        # return num_gt_pivot, permutate A
        new_pivot_idx = lower
        pivot_val = A[pivot_idx]
        #难点实在in-place重排数列，把pivot放到合适的位置
        # 把pivot放到最右边，技巧
        A[upper], A[pivot_idx] = A[pivot_idx], A[upper]
        for i in range(lower, upper):
            if A[i] > pivot_val:
                A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                new_pivot_idx += 1
        #把pivot移到所有比它大的数之后
        A[upper], A[new_pivot_idx] = A[new_pivot_idx], A[upper]
        return new_pivot_idx

    lower, upper = 0, len(A) - 1
    while lower <= upper:
        pivot_idx = random.randint(lower, upper)
        new_pivot_idx = partition(pivot_idx, lower, upper)
        if new_pivot_idx == k - 1:
            return A[k-1]
        elif new_pivot_idx > k - 1:
            upper = new_pivot_idx - 1
        else:
            lower = new_pivot_idx + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
