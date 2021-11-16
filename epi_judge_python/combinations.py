from typing import List
from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    # ref: https://www.youtube.com/watch?v=q0s6m7AiM7o
    res = []
    def backtrack(start, finished):
        if len(finished) == k:
            res.append(finished.copy())
            return
        # #pruning, improve time efficiency
        # remaining = k - len(finished)
        # # n - i + 1 >= remaining
        # # i <= n +1 - remaining
        # for i in range(start, n-remaining + 2):
        for i in range(start, n + 1):
            # finished.append(i)
            backtrack(i + 1, finished+[i]) #这里新建1个对象，就不用append和pop了
            # finished.pop()
    backtrack(1, [])
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
