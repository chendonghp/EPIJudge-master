import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    # TODO - you fill in here.
    # return []
    def left(tree):
        if not tree or (not tree.left and not tree.right):
            return
        exterior.append(tree)
        if tree.left:
            left(tree.left)
        else:
            left(tree.right)
    def right(tree):
        if not tree or (not tree.left and not tree.right):
            return
        if tree.right:
            right(tree.right)
        else:
            right(tree.left)
        exterior.append(tree)
    def leaves(tree):
        if tree:
            if not tree.left and not tree.right:
                exterior.append(tree)
                return
            leaves(tree.left)
            leaves(tree.right)

    if not tree:
        return []
    exterior=[tree]
    left(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right(tree.right)
    return exterior

    #边界情况很麻烦
    # left=[tree]
    # right=[]
    # leaf=[]
    # if tree.left:
    #     curr=tree.left
    #     while curr:
    #         left.append(curr)
    #         if curr.left:
    #             curr=curr.left
    #         else:
    #             curr=curr.right
    # if tree.right:
    #     curr=tree.right
    #     while curr:
    #         right.append(curr)
    #         if curr.right:
    #             curr=curr.right
    #         else:
    #             curr=curr.left
    #     right.reverse()
    # def leaf(tree):
    #     if tree:
    #         if not tree.left and not tree.right:
    #             return [tree]
    #         left = leaf(tree.left)
    #         right = leaf(tree.right)
    #         return left + right
    #     else:
    #         return []
    # leaf=leaf(tree)
    # if len(leaf) == 1: leaf=[]
    # if tree.left:leaf.pop(0)
    # if tree.right:leaf.pop()
    # return left+leaf+right

def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
