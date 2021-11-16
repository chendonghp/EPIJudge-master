from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    # return []
    from collections import deque
    layer_end='end'
    queue=deque()
    if tree:
        queue.append(tree)
        queue.append(layer_end)
    layers=[]
    current_layer=[]
    while queue:
        t=queue.popleft()
        if t=='end':
            layers.append(current_layer)
            current_layer=[]
            if queue:
                queue.append(layer_end)
        else:
            current_layer.append(t.data)
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
    return layers


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
