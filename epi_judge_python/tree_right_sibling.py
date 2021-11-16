import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    # TODO - you fill in here.
    # return
    # 递归解法
    # if not tree or not tree.left:
    #     return
    # left=tree.left
    # right=tree.right
    # while left:
    #     left.next=right
    #     left=left.right
    #     right=right.left
    # construct_right_sibling(tree.left)
    # construct_right_sibling(tree.right)

    #书上解法
    def visit_next_level(tree):
        while tree and tree.left:
            tree.left.next=tree.right
            tree.right.next=tree.next.left if tree.next else None
            tree=tree.next
    while tree and tree.left:
        visit_next_level(tree)
        tree = tree.left

def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
