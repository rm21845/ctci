"""Solution to 3.3: Stack of Plates."""

from ctci.structs.stack import Stack


class StackOfPlates(Stack):

    _MAX_SIZE = 10

    def __init__(self):
        self._array = [[]]

    def push(self, payload):
        if len(self._array[-1]) == self._MAX_SIZE:
            self._array.append([payload])
        self._array[-1].append(payload)
        
    def pop(self):
        return self._array[-1].pop()

    #needs testing
    def pop_at(self, index):
        if len(self._array[index]) != 1:
            return self._array[index].pop()
        value = self._array[index].pop()
        del self._array[index]
        return value 

    def peek(self):
        return self._array[-1][-1]