

class Node(object):
    def __init__(self, value, next_node=None, prev_node=None):
        self._next_node = next_node
        self._prev_node = prev_node
        self._value = value

    def __repr__(self):
        pass

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
        return self._next_node

    @value.setter
    def value(self, new_value):
        self._value = new_value    


class LinkedList(object):

    def __init__(self):
        self._head = None 
    
    def __repr__(self):
        pass

    def search(self, value):
        return 0

    def insert(self, value=None, index=None):
        return None

    def delete(self, value=None, index=None):
        return None

    def update(self, value, index):
        pass


class SinglyLinkedList(LinkedList):

    def __init__(self):
        #use super
        pass
    
    def __repr__(self):
        pass


class DoublyLinkedList(LinkedList):

    def __init__(self):
        #use super
        pass
    
    def __repr__(self):
        pass