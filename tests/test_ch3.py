import unittest
from ctci.chapter3 import threeinone, stackmin, stackofplates, \
     queueviastacks, sortstack, animalshelter


class TestThreeInOne(unittest.TestCase):
    pass 


class TestStackMin(unittest.TestCase):
    
    def setUp(self):
        self.a = stackmin.StackMin()

    def test_push_one(self):
        self.a.push(1)
        self.assertEqual(self.a.peek(), 1)

    def test_push_two(self):
        self.a.push(1)
        self.a.push(2)
        self.assertEqual(self.a.peek(), 2)

    def test_len_empty(self):
        self.assertEqual(len(self.a), 0)

    def test_len_one(self):
        self.a.push(1)
        self.assertEqual(len(self.a), 1)

    def test_len_multi(self):
        self.a.push(1)
        self.a.push(1)
        self.a.push(1)
        self.a.push(1)
        self.assertEqual(len(self.a), 4)
    
    def test_len_with_pop(self):
        self.a.push(1)
        self.a.pop()
        self.a.push(1)
        self.a.push(1)
        self.assertEqual(len(self.a), 2)

    def test_pop_one(self):
        self.a.push(1)
        self.assertEqual(self.a.pop(), 1)

    def test_pop_two(self):
        self.a.push(1)
        self.a.push(4)
        self.assertEqual(self.a.pop(), 4)

    def test_peek_one(self):
        self.a.push(1)
        self.assertEqual(self.a.peek(), 1)

    def test_peek_two(self):
        self.a.push(1)
        self.a.push(4)
        self.assertEqual(self.a.peek(), 4)

    def test_empty(self):
        self.assertTrue(self.a.is_empty())

    def test_not_empty(self):
        self.a.push(1)
        self.assertFalse(self.a.is_empty())

    def test_min_one(self):
        self.a.push(1)
        self.assertTrue(self.a.min(), 1)

    def test_min_two(self):
        self.a.push(1)
        self.a.push(2)
        self.assertTrue(self.a.min(), 1)

    def test_min_three(self):
        self.a.push(3)
        self.a.push(2)
        self.a.push(1)
        self.a.push(3)
        self.a.push(4)

        self.assertTrue(self.a.min(), 1)


class TestStackOfPlates(unittest.TestCase):
    pass 


class TestQueueViaStacks(unittest.TestCase):
    pass 


class TestSortStack(unittest.TestCase):
    pass 


class TestAnimalShelter(unittest.TestCase):
    pass 

if __name__ == '__main__':
    unittest.main()