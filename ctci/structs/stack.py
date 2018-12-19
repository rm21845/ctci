import numpy as np 


class Stack(object):

    def __init__(self, size= None):
        self._size = size or 1000
        self._array = np.empty(self._size)
        self._index = 0

    def __len__(self):
        return self._index

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def pop(self):
        value = self._array[self._index]
        self._index -= 1
        self._array[self._index] = None 
        return value 

    def push(self, payload):
        try:
            self._index += 1
            self._array[self._index] = payload
        except IndexError:
            self._resize()
            self._index += 1
            self._array[self._index] = payload

    def peek(self):
        return self._array[self._index]

    def is_empty(self):
        return self._index == 0
    
    def _resize(self):
        self._array.resize(self._index + int(self._index * 0.5)) 