import numpy as np 
from ctci.structs.linkedlist import SinglyLinkedList


class HashTable(object):

    def __init__(self, size=None):
        if size:
            self._size = size
        else:
            self._size = 1000 
        self._table = np.empty(self._size, SinglyLinkedList)

    def __getitem__(self, index):
        return self._table[index]

    def __len__(self):
        return len(self._table)

    @staticmethod
    def hash_fnv(value):
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
        return self._table[self.hash_fnv(data) % self._size].search(data).value

    def insert(self, value):
        index = self.hash_fnv(value) % self._size
        try:
            self._table[index].insert(value)
        except AttributeError:
            self._table[index] = SinglyLinkedList()
            self._table[index].insert(value)

    def delete(self, value):
        try:
            self._table[self.hash_fnv(value) % self._size].delete(value)
        except AttributeError:
            pass