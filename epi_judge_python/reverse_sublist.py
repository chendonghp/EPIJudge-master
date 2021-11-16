from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) :
    # TODO - you fill in here.
    # return None
    dummy_head=sublist_head=ListNode(0,L)
    for _ in range(1,start):
        sublist_head=sublist_head.next
    tail=sublist_head.next
    for _ in range(start,finish):
        current=tail.next
        sublist_head.next,current.next,tail.next=\
            current,sublist_head.next,current.next
    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
