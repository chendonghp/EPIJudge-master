from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    # return True
    brackets={')':'(','}':'{',']':'['}
    stack=[]
    for c in s:
        if c in brackets:
            if stack.pop()!=brackets[c]:
                return False
        else:
            stack.append(c)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
