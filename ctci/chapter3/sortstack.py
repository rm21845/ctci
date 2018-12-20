"""Solution to 3.5: Sort Stack."""

from ctci.structs.stack import Stack


def sort_stack(unsorted):
    temp = Stack()
    temp.push(unsorted.pop())
    while not unsorted.is_empty():
        popped = unsorted.pop()
        while popped > temp.peek():
            unsorted.push(temp.pop())
        temp.push(popped)
    return temp