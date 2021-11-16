from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    # TODO - you fill in here.
    # return 0
    order={'I':1,
           'V':5,
           'X':10,
           'L':50,
           'C':100,
           'D':500,
           'M':1000}
    sum=0
    i=0
    while i< len(s):
        if i+1<len(s) and order[s[i]] < order[s[i+1]]:
            sum+=order[s[i+1]]-order[s[i]]
            i+=1
        elif i+1<len(s) and order[s[i]] >= order[s[i+1]]:
            sum+=order[s[i]]
        else:
            sum+=order[s[i]]
        i+=1
    return sum

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
