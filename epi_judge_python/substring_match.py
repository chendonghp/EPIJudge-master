from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    # TODO - you fill in here.
    # return 0
    # #brute force
    # i=0
    # if len(t) == 0:
    #     return -1
    # while i <len(t):
    #     j=0
    #     pos=i
    #     if len(s)==0:
    #         return 0
    #     while s[j]==t[i]:
    #         if j==len(s)-1:
    #             return pos
    #         if i==len(t)-1:
    #             return -1
    #         j+=1
    #         i+=1
    #     if i==len(t)-1:
    #         return -1
    #     i=pos+1

    #rabin-karp algorith
    # hash function: ord(ch)%10
    t_hash = 1
    s_hash = 0
    if len(s) == 0:
        return 0

    for i in range(len(s)):
        s_hash = s_hash * 10 + ord(s[i]) % 10
        if i < len(s) - 1 and len(t)>=len(s):
            t_hash = t_hash * 10 + ord(t[i]) % 10
    for i in range(len(t) - len(s) + 1):
        t_hash = (t_hash % 10 ** (len(s) - 1)) * 10 + ord(t[i + len(s) - 1]) % 10
        if s_hash == t_hash and t[i:i + len(s)] == s:
            return i

    return -1






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
