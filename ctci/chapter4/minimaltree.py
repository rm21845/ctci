"""Solution to 4.2: Minimal Tree."""

from ctci.structs.bst import Node


def min_height(unique):
    node = Node(unique[int(len(unique)/2)])
    if unique[:int(len(unique)/2)]:
        node.left = min_height(unique[:int(len(unique)/2)])
    if unique[int(len(unique)/2)+1:]:
        node.right = min_height(unique[int(len(unique)/2)+1:])
    return node
