import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    # TODO - you fill in here.
    # return DuplicateAndMissing(0, 0)
    from functools import reduce
    len_=len(A)
    xor= reduce(lambda a,b: a^b, A) ^ reduce(lambda a,b: a^b, range(len_))
    if xor ==0:
        pos = 0
    else:
        i = 0
        n_xor=xor
        while n_xor % 2 !=1:
            i+=1
            n_xor >>= 1
        pos=1<<i
    # pos = xor & (~(xor-1))
    #一定要给初值, 如果A=[0, 0], 没有满足条件的元素，reduce就会报错。给初值就是防止这种情况。
    missing_or_dup = reduce(lambda a,b:a^b, [e for e in A if e & pos ],0 ) \
                     ^ reduce(lambda a,b: a^b, [e for e in range(len_) if e & pos],0)
    if missing_or_dup in A:
        dup=missing_or_dup
        missing = xor^dup
        return DuplicateAndMissing(dup,missing)
    else:
        missing = missing_or_dup
        dup = xor ^ missing
        return DuplicateAndMissing(dup, missing)

def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
