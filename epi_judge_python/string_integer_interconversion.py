from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    # return '0'
    neg=False
    if x<0:
        x=-x
        neg=True
    if x==0:
        return '0'
    s=[]
    while x>0:
        s.append(chr(x % 10+ord('0')))
        x=x//10
    if neg:
        s.append('-')
        return ''.join(list(reversed(s)))
    else:
        return ''.join(list(reversed(s)))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    # return 0
    sum=0
    if s[0] == '-':
        sign = -1
    else:
        sign = 1
    s=s.strip('+-')
    for n in s:
        sum=sum*10+ord(n)-ord('0')
    return sum*sign



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
