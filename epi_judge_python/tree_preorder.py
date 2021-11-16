from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    # return []
    #istree, get data, push onto stack,t=t.left
    #isNone, pop, t=t.right
    #解题模仿9.7
    stack=[]
    traversal=[]
    while tree or stack:
        if tree:
            traversal.append(tree.data)
            stack.append(tree)
            tree=tree.left
        else:
            tree=stack.pop()
            tree=tree.right
    return traversal

    # #Sol.2: 书上解法
    # stack,traversal=[tree], []
    # while stack:
    #     current=stack.pop()
    #     if current:
    #         traversal.append(current.data)
    #         stack.append(current.right)
    #         stack.append(current.left)
    # return traversal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
