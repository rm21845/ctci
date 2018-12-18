"""Solution to 2.2: Return Kth to Last."""

def find(to_find, k):
    """Finds the Kth to last element in LinkedList.

    uses two references to find the kth to last element
    within a linked list

    Args: 
        to_find: LinkedList containing kth element
        k: the kth to last position

    Returns:
        the kth node's data.
    """
    target = to_find.head
    for node in to_find:
        if k < 0:
            target = target.next_node
        k -= 1
    return target.value

        