import unittest
from ctci.structs.stack import Stack


class TestStackPush(unittest.TestCase):
    
    def setUp(self):
        self.a = Stack()

    def test_one(self):
        self.a.push(1)
        self.assertEqual(self.a.peek(), 1)

    def test_two(self):
        self.a.push(1)
        self.a.push(2)
        self.assertEqual(self.a.peek(), 2)

class TestStackLen(unittest.TestCase):
    
    def setUp(self):
        self.a = Stack()

    def test_empty(self):
        self.assertEqual(len(self.a), 0)

    def test_one(self):
        self.a.push(1)
        self.assertEqual(len(self.a), 1)

    def test_multi(self):
        self.a.push(1)
        self.a.push(1)
        self.a.push(1)
        self.a.push(1)
        self.assertEqual(len(self.a), 4)
    
    def test_with_pop(self):
        self.a.push(1)
        self.a.pop()
        self.a.push(1)
        self.a.push(1)
        self.assertEqual(len(self.a), 2)

    def test_with_pop_multi(self):
        self.a.push(1)
        self.a.pop()
        self.a.push(1)
        self.a.push(1)
        self.a.pop()
        self.assertEqual(len(self.a), 1)

class TestStackPop(unittest.TestCase):
    
    def setUp(self):
        self.a = Stack()

    def test_one(self):
        self.a.push(1)
        self.assertEqual(self.a.pop(), 1)

    def test_two(self):
        self.a.push(1)
        self.a.push(4)
        self.assertEqual(self.a.pop(), 4)

class TestStackPeek(unittest.TestCase):

    def setUp(self):
        self.a = Stack()

    def test_one(self):
        self.a.push(1)
        self.assertEqual(self.a.peek(), 1)

    def test_two(self):
        self.a.push(1)
        self.a.push(4)
        self.assertEqual(self.a.peek(), 4)


class TestStackIsEmpty(unittest.TestCase):
    
    def setUp(self):
        self.a = Stack()

    def test_empty(self):
        self.assertTrue(self.a.is_empty())

    def test_not_empty(self):
        self.a.push(1)
        self.assertFalse(self.a.is_empty())

if __name__ == '__main__':
    unittest.main()