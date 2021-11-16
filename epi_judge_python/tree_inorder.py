from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    # return []
    #书上解法
    # traversal=[]
    # stack=[]
    # while tree or stack:
    #     if tree:
    #         stack.append(tree)
    #         tree=tree.left
    #     else:
    #         tree=stack.pop()
    #         traversal.append(tree.data)
    #         tree=tree.right
    # return traversal

    #仿照9.8的思路，不过比preorder麻烦
    stack, traversal = [tree], []
    while stack:
        if current:
            stack.append(current.right)
            stack.append(current)
            current=current.left
        else:
            current = stack.pop()
            traversal.append(current.data)
    return traversal

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
