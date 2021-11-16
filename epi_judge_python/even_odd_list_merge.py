from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    # return None
    #two pointer point to even and odd number tail
    current=L
    if current and current.next:
        even,odd= L,L.next
    else:
        return L
    tail_even=False
    pre=None
    while current and current.next:
        tail_even=not tail_even
        pre=current
        tmp=current.next
        current.next=current.next.next
        current=tmp
    tail_even=not tail_even
    if tail_even:
        current.next=odd
    else:
        pre.next=odd
    return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
