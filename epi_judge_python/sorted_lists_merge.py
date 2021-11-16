from typing import Optional

from list_node import ListNode
from test_framework import generic_test

#直接遍历
def merge_two_sorted_lists2(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    # dummy_head=tail=ListNode()
    # while L1 and L2:
    #     if L1.data<L2.data:
    #         tail.next=L1
    #         L1=L1.next
    #     else:
    #         tail.next=L2
    #         L2=L2.next
    #     tail = tail.next
    # tail.next = L1 or L2
    # return dummy_head.next

    #没有使用dummy node
    if L1==None or L2==None:
        return L1 if L2 == None else L2
    if L1.data<L2.data:
        L = tmp = L1
        L1=L1.next
    else:
        L=tmp=L2
        L2=L2.next

    while L1 and L2:
        if L1.data<L2.data:
            tmp.next=L1
            tmp=L1
            L1=L1.next
        else:
            tmp.next = L2
            tmp = L2
            L2=L2.next
    tmp.next= L1 if L2 == None else L2
    return L

#使用dummy node
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    #结果链表先加入一个节点，就不用比较两个链表第一个节点的大小，继而也不用测试头节点是否为空。
    L=tmp=ListNode()
    #对比前面算法L的头节点赋值,手动加入dummy node省去了很多麻烦
    while L1 and L2:
        if L1.data<L2.data:
            tmp.next=L1
            tmp=L1
            L1=L1.next
        else:
            tmp.next=L2
            tmp=L2
            L2=L2.next
    tmp.next= L1 if L2==None else L2
    #返回时再去除头节点
    return L.next
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
