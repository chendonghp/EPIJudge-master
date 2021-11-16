from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> list[str]:
    # TODO - you fill in here.
    # return []
    ips=[]
    for i in range(1,len(s)-2):
        if int(s[0:i]) < 256 and (i-0 == 1 if s[0:i][0]=='0' else True) and len(s)-i<=3*3:
            for j in range(i+1,len(s)-1):
                if int(s[i:j]) < 256 and (j-i == 1 if s[i:j][0]=='0' else True) and len(s)-j<=3*2:
                    for k in range(j+1,len(s)):
                         if int(s[j:k]) <256 and int(s[k:]) <256 and (k-j== 1 if s[j:k][0]=='0' else True)\
                            and (len(s)-k == 1 if s[k:][0]=='0' else True) and len(s)-k<=3:
                            ips.append('.'.join([s[0:i],s[i:j],s[j:k],s[k:]]))

    return ips

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
