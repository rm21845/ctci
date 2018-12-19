"""Solution 2.8: Loop Detection."""


def detect(llist):
    runner = llist.head

    for node in llist:
        if runner is node:
            return node 
        try:
            runner = llist.next_node.next_node
        except AttributeError:
            pass