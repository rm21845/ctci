"""Binary Search Tree Implementation.

RMIT: 
http://www.cs.rmit.edu.au/online/blackboard/chapter/05/documents/contribute/chapter/11/binary-tree-ops.html
"""

class Node(object):

    def __init__(self, value):
        self._parent = None
        self._right = None
        self._left = None 
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node 

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def is_leaf(self):
        if not self.left or self.right: return True
        return False

    def has_parent(self):
        if self._parent: return True
        return False


class Tree(object):

    def __init__(self):
        self._root = None

    def __len__(self):
        pass

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node

    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return current
            elif current.left and current.left.value >= value:
                current = current.left
            elif current.right and current.right.value <= value:
                current = current.right
            else: break

    def _delete(self, value, node):
        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        elif node.right and node.left:
            node.value = self.minimum(node.right).value
            node.right = self._delete(node.value, node.right)
        elif node.right or node.left:
            if node.right:
                node = node.right
            else:
                node = node.left
        elif not node.right and not node.left:
            node = None
        return node

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _insert(self, value, node):
        if not node:
            node = Node(value)
        elif node.value and value < node.value:
            node.left = self._insert(value, node.left)
        elif node.value and value > node.value:
            node.right = self._insert(value, node.right)
        return node 

    def insert(self, value):
        self.root = self._insert(value, self.root)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.value)
            self._in_order(node.right)
            
    def in_order(self):
        self._in_order(self.root)

    def _pre_order(self, node):
        if node:
            print(node.value)
            self._pre_order(node.left)
            self._pre_order(node.right)
            
    def pre_order(self):
        self._pre_order(self.root)

    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.value)

    def post_order(self):
        self._post_order(self.root)

    def minimum(self, node=None):
        current = node or self.root        
        while current.left:
            current = current.left
        return current

    def maximum(self, node=None):
        current = node or self.root        
        while current.right:
            current = current.right
        return current

    def is_full(self):
        pass

    def is_complete(self):
        pass 

    def is_perfect(self):
        pass

    def is_empty(self):
        if not self.root: return True
        return False