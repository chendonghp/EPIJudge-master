from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    # TODO - you fill in here.
    # return []
    # backtracking + pruning
    def backtracking(i, parens):
        if len(parens) == 2*num_pairs:
            result.append(parens)
            return
        for p in bracket:
            n_left_brac = parens.count('(')
            if p == '(' and  n_left_brac < num_pairs:
                backtracking(i+1, parens+'(')
            elif p == ')' and len(parens) - n_left_brac < n_left_brac:
                backtracking(i+1, parens+')')

    result = []
    bracket = ['(', ')']
    backtracking(0, '')
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
