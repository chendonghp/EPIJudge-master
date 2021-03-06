import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    # return None
    # #direct sol. to store the visited
    # visited=set()
    # current=head
    # while current:
    #     # id(obj) return obj memery address(identity),
    #     if id(current) in visited:
    #         return current
    #     visited.add(id(current))
    #     current=current.next
    # return None

    # fast = slow = head
    # while True:
    #     if not (fast and fast.next):
    #         return None
    #     fast, slow = fast.next.next, slow.next
    #     #这里写if fast == slow: 程序会中断
    #     # 参见Mark Lutz, Learning python, p300 comparison
    #     # == 会检查两边对象内部的结构是否都相等，这里链表有环状结构，可能会引发死循环。
    #     # 用is来比较只检查地址, 可以避免上述情况
    #     if fast is slow:
    #         break
    # fast = head
    # # fast ！= slow 也会出错
    # while fast is not slow:
    #     fast, slow = fast.next, slow.next
    # return slow

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow  # sTow is the start of cycle
    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
