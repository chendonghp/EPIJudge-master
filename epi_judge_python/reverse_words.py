import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # TODO - you fill in here.
    # return
    # # space complexity is O(n)
    # begin=0
    # words=[]
    # for i in range(len(s)):
    #      if s[i] ==' ':
    #          words.append(s[begin:i])
    #          begin=i+1
    #      if i==len(s)-1:
    #         words.append(s[begin:])
    #
    # for i in range(len(words)//2):
    #     words[i],words[~i]=words[~i],words[i]
    # i=0
    # s=[]
    # while i < len(words):
    #     s.extend(words[i]+[' ']) if i<len(words)-1 else s.extend(words[i])
    #     i+=1
    # return s

    #space complexity is O(n), in place
    def reverse_word(word,b,e):
        while b<e:
            word[b],word[e]=word[e],word[b]
            b+=1
            e-=1

    begin=0
    for i in range(len(s)):
        if s[i]==' ':
            reverse_word(s,begin,i-1)
            begin=i+1
    reverse_word(s,begin,len(s)-1)
    #reverse whole words
    reverse_word(s,0,len(s)-1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
