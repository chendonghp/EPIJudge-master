import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    # return None
    #check if l0 and l1 has a cycle
    #if one don't have a cycle, call cycle free algorithms
    #if one have cycle,find branch point, check common point in or out of cycle
    #if out cycle, using cycle free algorithms
    #if in cycle, select a ele in cycle, check if second list pass through it
    #if pass, return 2 or 1(common) branch point, else return None
    from is_list_cyclic import has_cycle
    from do_terminated_lists_overlap import overlapping_no_cycle_lists
    if has_cycle(l0) and has_cycle(l1):
        if has_cycle(l0) is has_cycle(l1):
            current_l0,current_l1=l0,l1
            len_before_loop_l0,len_before_loop_l1=0,0
            while current_l0 is not has_cycle(l0):
                len_before_loop_l0+=1
                current_l0=current_l0.next
            while current_l1 is not has_cycle(l1):
                len_before_loop_l1+=1
                current_l1=current_l1.next
            diff=len_before_loop_l0-len_before_loop_l1
            if diff<0:
                llong,lshort=l1,l0
            else:
                llong, lshort = l0, l1
            for _ in range(abs(diff)):
                llong=llong.next
            while lshort is not llong and lshort is not has_cycle(10):
                lshort=lshort.next
                llong=llong.next
            return lshort if lshort is llong else has_cycle(10)
        # 不同的分支点
        #这里需要注意：一个链表是是循环链表，两个分支点就变成一个,这里情况比较复杂，书上的分类可以规避这个问题
        second_list=has_cycle(l0)
        while second_list is not has_cycle(l0):
            if second_list==has_cycle(l1):
                return has_cycle(l1)
            second_list=second_list.next
        return None

    elif not has_cycle(l0) and not has_cycle(l1):
        return overlapping_no_cycle_lists(l0, l1)
    else:#has_cycle(l0) and not has_cycle(l1) or has_cycle(l1) and not has_cycle(l0):
        return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
