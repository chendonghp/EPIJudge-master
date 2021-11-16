from test_framework import generic_test


def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    # return ''
    s='1'
    for i in range(1,n):
        begin=0
        num=1
        tmp_s=[]
        for j in range(len(s)):
            #把前面的算好
            if s[j]!=s[j-1] and j>0:
                tmp_s.extend([str(num) + s[j-1]])
                begin=j
                num=1
            elif s[j]==s[j-1] and j>0:
                num+=1
            #到边界，把边界也算好
            if j == len(s) - 1:
                    tmp_s.extend([str(num) + s[j]])
        s=''.join(tmp_s)
    return s

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
