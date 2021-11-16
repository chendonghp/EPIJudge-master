from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
    # return True
    #1. 找到中间点
    if not L:
        return True
    slow=fast=L
    while fast and fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    # 2. reverse second linked list
    dummy_node=pre=ListNode(None,None)
    current=slow.next
    while current:
        next=current.next
        current.next=pre
        pre=current
        current=next
    # 3. 逐个比较是否相同
    while pre.next:#最后增加了一个dummy node，所以要用pre.next
        if pre.data!=L.data:
            return False
        pre,L=pre.next,L.next
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
