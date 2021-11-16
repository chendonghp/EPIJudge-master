from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    # return None
    first_iter=L
    dummy_head=ListNode(0,L)
    second_iter=dummy_head
    for _ in range(k):
        first_iter=first_iter.next
    while first_iter:
        first_iter=first_iter.next
        second_iter=second_iter.next
    second_iter.next=second_iter.next.next
    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
