from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    # TODO - you fill in here.
    # return ''
    decode_str=[]
    length=0
    for i in range(len(s)):
        if ord('0')<=ord(s[i])<=ord('9'):
            length=length*10+int(s[i])
        else:
            decode_str.append(s[i]*length)
            length=0
    decode_str=''.join(decode_str)
    return decode_str

def encoding(s: str) -> str:
    # TODO - you fill in here.
    # return ''
    # num=1
    # rle= []
    # for i in range(1,len(s)):
    #     if s[i]==s[i-1]:
    #         num+=1
    #     elif s[i]!=s[i-1]:
    #         rle.extend(str(num)+s[i-1])
    #         num=1
    #     if i==len(s)-1:
    #         rle.extend(str(num) + s[i])
    # if len(s) ==1:
    #     return '1'+s
    # rle=''.join(rle)
    # return rle

    #书上的解法似乎简洁
    num, rle = 1, []
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            rle.extend(str(num) + s[i - 1])
            num = 1
        elif s[i] == s[i - 1]:
            num += 1
    rle = ''.join(rle)
    return rle

def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
