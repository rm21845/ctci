"""Solution to 2.5: Sum Lists."""

import itertools as it
from ctci.structs.linkedlist import Node, SinglyLinkedList


def sum(list_a, list_b):
    """Calculates the sum of LinkedList data.

    calculates the sum of linked list data in a reverse
    manner. The data is then added in a reverse manner 
    into a new LinkedList.

    Args: 
        list_a: a linked list containing an operand
        list_b: a linked list containing an operand

    Returns:
        a LinkedList containing the sum of the operand
        args in a reverse ordering.
    """

    sum_list = SinglyLinkedList()
    temp = list()
    total = 0 
    remainder = 0

    for nodes in it.zip_longest(list_a, list_b):
        total = remainder 
        if nodes[0] and nodes[1]:
            total += nodes[0].value + nodes[1].value
        elif nodes[0]:
            total += nodes[0].value
        elif nodes[1]:
            total += nodes[1].value
        temp.append(total % 10)
        remainder = total // 10
    [sum_list.insert(item) for item in reversed(temp)]
    return sum_list

def add_zeroes(list_a, list_b):
    """Adds zeroes to list to zero out length difference.

    calculates the difference in length between two LinkedLists.
    the shorter LinkedList is prepended with zeroes to close the
    difference.

    Args: 
        list_a: a linked list containing integers
        list_b: a linked list containing integers

    """
    diff_range = abs(len(list_a) - len(list_b))
    if len(list_a) > len(list_b):
        for i in range(diff_range):
            list_b.insert(0)
    elif len(list_a) < len(list_b):
        for i in range(diff_range):
            list_a.insert(0)

def follow_up(list_a, list_b):
    """Calculates the sum of LinkedList data.

    calculates the sum of linked list data in a reverse
    manner. The data is then added in a foward manner 
    into a new LinkedList.

    Args: 
        list_a: a linked list containing an operand
        list_b: a linked list containing an operand

    Returns:
        a LinkedList containing the sum of the operand
        args in a foward ordering.
    """
    sum_list = SinglyLinkedList()
    total = 0 

    add_zeroes(list_a, list_b)
    for nodes in it.zip_longest(list_a, list_b):
        total = (total * 10) + nodes[0].value + nodes[1].value
    [sum_list.insert(int(value)) for value in reversed(str(total))]
    return sum_list