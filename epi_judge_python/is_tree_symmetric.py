from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    # return True
    def postorder_left(tree,left):
        if tree:
            postorder_left(tree.left,left)
            postorder_left(tree.right,left)
            left.append(tree.data)
    def postorder_right(tree,right):
        if tree:
            postorder_right(tree.right, right)
            postorder_right(tree.left, right)
            right.append(tree.data)
    if not tree:
        return True
    left=[]
    right=[]
    postorder_left(tree.left,left)
    postorder_right(tree.right,right)
    return left == right

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
