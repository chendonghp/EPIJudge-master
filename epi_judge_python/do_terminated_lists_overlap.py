import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    # TODO - you fill in here.
    # return ListNode()

    #1. storing visited nodes\
    #leetcode 上可以通过测试，这里不行
    # visited=[]
    # current=l0
    # while current:
    #     visited.append(id(current))
    #     current=current.next
    # current=l1
    # while current:
    #     if id(current) in visited:
    #         return current
    #     current=current.next
    # return None

    def length(llist):
        l = llist
        length = 0
        while l:
            length += 1
            l = l.next
        return length

    diff = length(l0) - length(l1)
    if diff < 0:
        llong, lshort = l1, l0
    else:
        llong, lshort=l0, l1
    for _ in range(abs(diff)):
            llong = llong.next
    while lshort and lshort is not llong:
        llong, lshort = llong.next, lshort.next
    return lshort


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
