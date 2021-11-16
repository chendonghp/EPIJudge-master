import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    # return None
    #这个方法太麻烦
        #find the first pos >=k
            #区分大于还是等于
        #record 2 addr p(<=k) and p(>k)
        #iter remaining, if i<=k, insert after p(i<k)
            #if i=k, p(<=k) don't change
            #else p(<=k) +=1
    less_x_head=ListNode(0,None)
    equal_x_head=ListNode(0,None)
    great_x_head=ListNode(0,None)
    pos=[less_x_head,equal_x_head,great_x_head]
    current=l
    while current:
        if current.data<x:
            pos[0].next=current
            pos[0]=current
        elif current.data==x:
            pos[1].next=current
            pos[1]=current
        else:
            pos[2].next=current
            pos[2]=current
        current=current.next
    pos[2].next=None
    pos[1].next=great_x_head.next
    pos[0].next=equal_x_head.next
    return less_x_head.next



def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
