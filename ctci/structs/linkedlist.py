

class Node():
    """A node for use with linked lists.

    Represents nodes uitable for either a singly linked
    list or a doubly linked list (or a circular list).

    Attributes:
        _next_node: a reference to another node in a list
        _prev_node: a reference to another node in a list
        _value: payload for the node
    """

    def __init__(self, value, next_node=None, prev_node=None):
        """Inits Node class with a value [next_node and prev_node]."""
        self._next_node = next_node
        self._prev_node = prev_node
        self._value = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, new_node):
        self._next_node = new_node

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, new_node):
        self._prev_node = new_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value    


class LinkedList(object):
    """Base class for Linked Lists

    A base class that is inherited by the SinglyLinkedList
    and DoublyLinkedList. LinkedList provides search, delete,
    and insert opretations.

    Attributes:
        _head: the top or most recent node in the list
    """

    def __init__(self):
        """Inits LinkedList with a head."""
        self._head = None 

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, new_node):
        self._head = new_node

    def search(self, value):
        """Search for first occurence of value given.

        Each node within the LinkedList instance is traversed
        until the first occurence of a given value is found. 
        
        Args:
            value: a value within a node

        Returns:
            a node containing the first occurence of the 
            value within the list. If the value is not found
            within the list, None is returned.
        """
        try:
            current = self.head
            while True:
                if self.head.value != value:
                    current = current.next_node
                else:
                    return current
        except AttributeError:
            pass

    def insert(self, value):
        """Insert value given at the head of LinkedList.
        
        inserts a value into a new node that will be inserted into
        the head of the LinkedList. If there is a current head, 
        the new node will be given head and the previous head will
        become the new nodes next reference.

        Args: 
            value: the value to insert into the new head node
        """
        if self.head:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node
        else: 
            new_node = Node(value)
            self.head = new_node

    def delete(self, value):
        """Delete first occurence of value given.
        
        traverses through the list and searches for the node
        with the first occurence of the given value. Upon discovery, 
        the node is deleted by breaking the previous node's reference 
        to the target node and reassigning the reference to the next node.
        """
        try:
            current = self.head
            if current.value == value:
                self.head = self.head.next_node
            else:
                previous = self.head 
                current = self.head.next_node
                while True:
                    if current.value != value:
                        previous = current
                        current = current.next_node
                    else:
                        previous.next_node = current.next_node
                        break
        except AttributeError:
            pass


class SinglyLinkedList(LinkedList):
    """A SinglyLinked List implementation.

    A class that inheritances LinkedList. It provides
    the operations given by LinkedList. It's nodes only
    have a reference to the next node in the list.
    """

    def __init__(self):
        """Inits SinglyLinkedList and inherits LinkedList Init."""
        super().__init__()


class DoublyLinkedList(LinkedList):
    """A DoublyLinked List implementation.

    A class that inheritances LinkedList. It provides
    the operations given by LinkedList. It's nodes
    have a reference to the next node and previous node in the list.
    """

    def __init__(self):
        """Inits DoublyLinkedList and inherits LinkedList Init."""
        super().__init__()

    def insert(self, value):
        """Insert value given at the head of LinkedList.
        
        inserts a value into a new node that will be inserted into
        the head of the LinkedList. If there is a current head, 
        the new node will be given head and the previous head will
        become the new nodes next reference. The previous head will 
        also take the new node as it's previous reference.

        Args: 
            value: the value to insert into the new head node
        """
        if self.head:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        else: 
            new_node = Node(value)
            self.head = new_node

    def delete(self, value):
        """Delete first occurence of value given.
        
        traverses through the list and searches for the node
        with the first occurence of the given value. Upon discovery, 
        the node is deleted by breaking the previous node's reference 
        to the target node and reassigning the reference to the next node. 
        the node next node will reassing it's previous reference to the node
        before the target node.
        """
        try:
            current = self.head
            if current.value == value:
                self.head = self.head.next_node
            else:
                previous = self.head 
                current = self.head.next_node
                while True:
                    if current.value != value:
                        previous = current
                        current = current.next_node
                    else:
                        previous.next_node = current.next_node
                        current.next_node.prev_node = previous
                        break
        except AttributeError:
            pass