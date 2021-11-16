from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    # return 0

    # # 1. brute force
    # x = str(x)
    # x = list(x)
    # t = []
    # for i in range(len(x)):
    #     t.append(x[len(x) - i - 1])
    # if t[-1]=='-':
    #     t.insert(0,'-')
    #     del(t[-1])
    # t = ''.join(t)
    # return int(t)

    # make use of modulus
    # 负数取模比较麻烦，这里设置了一个flag变量把它转换成正整数来处理。
    # ？有没有更general的处理方式
    flag=True
    if x<0:
        flag= False
        x=-x
    ts = 0
    while x!=0:
        ts*=10
        t=x % 10
        x=x // 10
        ts+=t
    if not flag:
        ts=-ts
    return ts


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
