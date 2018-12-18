"""A HashTable Implmentation.

A HashTable implementation that uses an array as an underlying
data structure for indexing. Each element in the array is made 
up of a LinkedList to resolve collisions via chaining. The FNV-1a
hashing algorithm in 64 bits is employed for hashing.

.. FNV-1a:
   http://www.isthe.com/chongo/tech/comp/fnv/

"""

import numpy as np 
from ctci.structs.linkedlist import SinglyLinkedList


class HashTable(object):

    def __init__(self, size=None):
        """Inits HashTable with a starting size."""
        if size:
            self._size = size
        else:
            self._size = 1000 
        self._table = np.empty(self._size, SinglyLinkedList)

    def __getitem__(self, index):
        """Returns a LinkedList within the HashTable."""
        return self._table[index]

    def __len__(self):
        """Returns the size of the Hashtable."""
        return len(self._table)

    @staticmethod
    def hash_fnv(value):
        """FNV-1a hashing function.

        the hashing function which takes in all 
        the data used for array indexing.

        Args: 
            value: the payload being entered into the HashTable.

        Returns: 
            a hash value given the inputted payload.
        """

        OFFSET_BASIS_64 = 14695981039346656037
        FNV_PRIME_64 = 1099511628211
        if isinstance(value, str):
            octets = bytes(value, 'utf-8')
        else:
            octets = bytes(value)

        hash = OFFSET_BASIS_64
        for byte in octets:
            hash ^= byte
            hash *= FNV_PRIME_64
        return hash

    def search(self, data):
        """Searches HashTable for a payload."""

        try:
            return self._table[self.hash_fnv(data) % self._size].search(data).value
        except AttributeError:
            pass
            
    def insert(self, value):
        """Inserts a payload into the HashTable."""

        index = self.hash_fnv(value) % self._size
        try:
            self._table[index].insert(value)
        except AttributeError:
            self._table[index] = SinglyLinkedList()
            self._table[index].insert(value)

    def delete(self, value):
        """Deletes a payload from the HashTable."""
        
        try:
            self._table[self.hash_fnv(value) % self._size].delete(value)
        except AttributeError:
            pass