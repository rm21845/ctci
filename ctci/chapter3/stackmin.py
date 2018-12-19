"""Solution to 3.2: Stack Minimum."""

from ctci.structs.stack import Stack


class StackMin(Stack):

    def __init__(self):
        super().__init__()

    def push(self, payload):
        if not self.is_empty() and payload > self.min():
            payload = (payload, self.min())
        else:
            payload = (payload, payload)
        self._array.append(payload)

    def min(self):
        if self._array:
            return self._array[-1][1]

    def peek(self):
        if self._array:
            return self._array[-1][0]

    def pop(self):
        return self._array.pop()[0]