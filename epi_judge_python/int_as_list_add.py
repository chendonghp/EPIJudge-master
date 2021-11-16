from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    # return None
    carry=0
    L=L1
    prev=None
    while L1 and L2:
        tmp=L1.data
        L1.data=(tmp+L2.data+carry) % 10
        carry =(tmp+L2.data+carry) // 10
        prev=L1
        L1=L1.next
        L2=L2.next
    if L2:
        prev.next=L2
        L1=L2
    while L1:
        tmp=L1.data
        L1.data=(carry+tmp)%10
        carry=(carry+tmp)//10
        prev=L1
        L1=L1.next
    if carry != 0:
        prev.next=ListNode(carry,None)
    return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
