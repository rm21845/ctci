"""Solution to 2.3: Delete Middle Node."""


def delete(node):
    """Removes a given node from a LinkedList.

    replaces each node with the next nodes value in 
    order to reaplace the data within a node. the last 
    node in the list has its reference point removed.

    Args:
            node: the node to be deleted.
    """
    while node.next_node:
        node.value = node.next_node.value
        node = node.next_node
        