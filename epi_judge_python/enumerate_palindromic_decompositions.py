from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    # TODO - you fill in here.
    # return []
    def backtracking(i, partition):
        # 当前层的迭代
        # |->
        # |-->
        # |--->
        # |---->
        # |----->
        # |------>
        # .......
        # |----------------------->|
        if i == len(text):
            res.append(partition.copy())
        for j in range(i+1, len(text)+1):
            word = text[i:j]
            if word == word[::-1]:
                backtracking(j, partition+[word])
    res = []
    backtracking(0, [])
    return res

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))

