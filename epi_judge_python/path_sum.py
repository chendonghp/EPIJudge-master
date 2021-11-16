from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    # TODO - you fill in here.
    # return True
    #跟9.5解题相似,要另外传入一个参数，记录先前的信息
    def sum_path(tree,sum_):
        if not tree:
            return False
        sum_+=tree.data
        if not tree.left and not tree.right:
            return sum_==remaining_weight
        return sum_path(tree.left, sum_) or sum_path(tree.right, sum_)
    return sum_path(tree, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
