"""Solution to 3.2: Stack Minimum."""

import numpy as np
from ctci.structs.stack import Stack


class StackMin(Stack):

    def __init__(self, size=None):
        self._size = size or 1000
        self._array = np.empty(self._size, dtype=tuple)
        self._index = 0

    def push(self, payload):
        if not self.is_empty() and payload > self.min():
            payload = (payload, self.min())
        else:
            payload = (payload, payload)
        try:
            self._index += 1
            self._array[self._index] = payload
        except IndexError:
            self._resize()
            self._index += 1
            self._array[self._index] = payload

    def min(self):
        return self._array[self._index][1]

    def peek(self):
        return self._array[self._index][0]

    def pop(self):
        value = self._array[self._index]
        self._index -= 1
        self._array[self._index] = None 
        return value[0] 