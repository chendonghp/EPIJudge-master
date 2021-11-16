import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    # return 0
    #forward pass to compute the final length
    #当索引来回跳跃，非均匀变化（增加或减少）使用while
    #索引均匀变化时，使用for-loop

    ## 用两个索引，一个用来检查，一个用来赋值
    l=0
    i=0
    n_a=0
    while i<size:
        if s[i] == 'b':
            s[l]=s[i+1]
        else:
            s[l] = s[i]
            l+=1
            if s[i]=='a':
                n_a+=1
        i+=1
    s[l:size]=''
    size = l
    l+=n_a
    final_size=l
    for i in reversed(range(size)):
        if s[i]== 'a':
            s[l-2:l]=['d','d']
            l-=2
        else:
            s[l-1]=s[i]
            l-=1
    return final_size

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
