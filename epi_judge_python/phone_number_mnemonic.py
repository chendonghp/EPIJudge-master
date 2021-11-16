from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> list[str]:
    # TODO - you fill in here.
    # return []
    #用具体例子来帮助理解
    num_ch={'0': ['0'],
            '1': ['1'],
            '2': ['A','B','C'],
            '3': ['D','E','F'],
            '4': ['G','H','I'],
            '5': ['J','K','L'],
            '6': ['M','N','O'],
            '7': ['P','Q','R','S'],
            '8': ['T','U','V'],
            '9': ['W','X','Y','Z']}
    total_num=1
    for s in phone_number:
        total_num*=len(num_ch[s])
    # print(total_num)
    strings=[]
    for i in range(total_num):
        tmp_string=[]
        dividend=i
        for s in phone_number:
            tmp_string.append(num_ch[s][dividend%len(num_ch[s])])
            dividend=dividend//len(num_ch[s])
        strings.append(''.join(tmp_string))
    return strings

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
