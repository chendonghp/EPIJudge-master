from test_framework import generic_test

import math

def is_palindrome_number(x: int) -> bool:
    # # TODO - you fill in here.
    # return True
    # # 1. b.f.
    # i=0
    # x=str(x)
    # while i< len(str(x))//2:
    #     if x[i] != x[-i-1]:
    #         return False
    #     i+=1
    # return True

    #细节容易出错。
    if x < 0:
        return False
    if x== 0:
        return True
    l = math.floor(math.log10(x))+1
    ms = 10 ** (l-1)
    while ms>0:
        if x % 10 != x // ms:
            return False
        x %= ms
        x //=10
        l-=2
        ms //=100
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
