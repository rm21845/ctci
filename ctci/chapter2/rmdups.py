"""Solution to 2.1: Remove Duplicates."""

from ctci.structs.hashtable import HashTable
from ctci.structs.linkedlist import SinglyLinkedList


def remove_with_table(to_remove):
    """Removes Duplicates in a LinkedList.
    
    duplicates are removed from a linked list by
    storing values in a temporary hash table and 
    removing duplicates on subsequent occurences.

    Args:
        to_remove: linked list which will have 
        duplicates removed.
    """
    table = HashTable()
    current = to_remove.head
    table.insert(current.value)

    while current.next_node:
        if table.search(current.next_node.value):
            to_remove.delete(current.next_node.value)
        else:
            table.insert(current.next_node.value)
        current = current.next_node
        
def remove_with_sort(to_remove):
    """Removes duplicates in a LinkedList.
    
    duplicates are removed from the lLinkedList
    by using two pointers to the linked list where
    one is used as a marker and the runner pointer
    is used to remove duplicate occurences of the 
    marked value.

    Args:
        to_remove: linked list which will have duplicates
        removed.
    """
    slow = to_remove.head
    runner = to_remove.head

    while slow:
        while runner:
            if runner.next_node:
                if slow.value == runner.next_node.value:
                    runner.next_node = runner.next_node.next_node
            runner = runner.next_node
        slow = slow.next_node
        try:
            runner = slow.next_node
        except:
            pass