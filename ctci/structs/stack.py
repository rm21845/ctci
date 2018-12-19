

class Stack(object):

    def __init__(self):
        self._array = list()

    def __len__(self):
        return len(self._array)

    def pop(self):
        return self._array.pop()

    def push(self, payload):
        self._array.append(payload)

    def peek(self):
        if self._array:
            return self._array[-1]

    def is_empty(self):
        return len(self._array) == 0
  