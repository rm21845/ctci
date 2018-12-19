from ctci.structs.stack import Stack


class QueueViaStacks(Stack):

    def __init__(self):
        self._main = Stack()
        self._temp = Stack()
        self._prior_remove = False

    def add(self, payload):
        if self._prior_remove:
            self._prior_remove = False
            while not self._temp.is_empty():
                self._main.push(self._temp.pop())
        self._main.push(payload)

    def remove(self):
        if self._prior_remove:
            return self._temp.pop()

        while not self._main.is_empty():
            self._temp.push(self._main.pop())
        self._prior_remove = True
        return self._temp.pop()

    def peek(self):
        if self._prior_remove:
            return self._temp.peek()

        while not self._main.is_empty():
            self._temp.push(self._main.pop())
        self._prior_remove = True
        return self._temp.peek()
    
    def is_empty(self):
        return len(self._main) == 0 and len(self._temp) == 0