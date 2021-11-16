import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def in_tree(tree, node):
    if tree:
        if node == tree:
            return True
        if in_tree(tree.left, node) or in_tree(tree.right, node):
            return True
from collections import deque
def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    # return None
    # #把两个节点的路径都算出来，然后得到LCA
    # def path(tree, node):
    #     if tree:
    #         if tree == node:
    #             q = deque()
    #             q.appendleft(tree)
    #             return q
    #         l = path(tree.left, node)
    #         if l:
    #             l.appendleft(tree)
    #             return l
    #         r = path(tree.right, node)
    #         if r:
    #             r.appendleft(tree)
    #             return r
    # path0=path(tree,node0)
    # path1=path(tree,node1)
    # i=0
    # for n0,n1 in zip(path0,path1):
    #     if n0 != n1:
    #         break
    #     i+=1
    # return path0[i-1]
    ##run time: 82, 10s

    #书上第一个暴力解法
    if tree == node0 or tree == node1 or (in_tree(tree.left,node0) and in_tree(tree.right, node1)) or (in_tree(tree.left,node1) and in_tree(tree.right, node0)):
        return tree
    elif in_tree(tree.left, node0):
        return lca(tree.left,node0,node1)
    else:
        return lca(tree.right,node0,node1)
    #runtime: 112, 10


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
