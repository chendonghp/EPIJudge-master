from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    # return True
    # if balanced, retrun height.
    def check_tree(tree):
        if not tree:
            return True, 0
        balanced_left, height_left = check_tree(tree.left)
        balanced_right, height_right = check_tree(tree.right)
        if balanced_left and balanced_right:
            return abs(height_left-height_right)<=1, max(height_left,height_right)+1
        else:
            return False,max(height_left,height_right)+1
    return check_tree(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
