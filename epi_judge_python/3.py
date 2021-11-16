from typing import List

def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    # TODO - you fill in here.
    # return []

    def backtracking(i, parens):
        if len(parens) == 2*num_pairs:
            if parens.count('(') == len(parens) // 2:
                result.append(parens)
            return
        for p in bracket:
            if p == '(':
                backtracking(i+1, parens+'(')
            elif p == ')' and parens.count(')') < len(parens) - parens.count(')'):
                backtracking(i+1, parens+')')

    result = []
    bracket = ['(', ')']
    backtracking(0, '')
    return result


print(generate_balanced_parentheses(3))
