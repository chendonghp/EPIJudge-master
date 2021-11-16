from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    # return ''
    if num_as_string=='0':
        return num_as_string
    import functools
    neg= (num_as_string[0] == '-')
    _ten=functools.reduce(
            lambda sum,n: sum*b1+(ord(n)-ord('0') if ord(n)<ord('A') else ord(n)-ord('A')+10),num_as_string[num_as_string[0] in '-+':],0)
    s = []
    while _ten>0:
        s.append(chr(_ten % b2-10+ord('A')) if _ten % b2 > 9 else chr(_ten % b2+ord('0')))
        _ten=_ten // b2
    if neg:
        s.append('-')
    return ''.join(list(reversed(s)))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
