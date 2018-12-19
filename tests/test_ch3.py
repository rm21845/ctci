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


class TestQueueViaStacks(unittest.TestCase):
    
    def setUp(self):
        self.a = queueviastacks.QueueViaStacks()

    def test_is_empty(self):
        self.assertTrue(self.a.is_empty())

    def test_is_not_empty(self):
        self.a.add(1)
        self.assertFalse(self.a.is_empty())

    def test_add_one(self):
        self.a.add(1)
        self.assertEqual(self.a.remove(), 1)

    def test_add_two(self):
        self.a.add(1)
        self.a.add(2)
        self.assertEqual(self.a.remove(), 1)

    def test_add_three(self):
        self.a.add(1)
        self.a.add(2)
        self.a.add(3)
        self.a.add(4)
        self.a.add(5)
        self.assertEqual(self.a.remove(), 1)

    def test_remove_one(self):
        self.a.add(1)
        self.a.add(2)
        self.a.add(3)
        self.a.add(4)
        self.a.add(5)
        self.a.remove()
        self.assertEqual(self.a.remove(), 2)

    def test_remove_two(self):
        self.a.add(1)
        self.a.add(2)
        self.a.add(3)
        self.a.add(4)
        self.a.add(5)
        self.a.remove()
        self.a.remove()
        self.assertEqual(self.a.remove(), 3)

    def test_remove_three(self):
        self.a.add(1)
        self.a.add(2)
        self.a.add(3)
        self.a.remove()
        self.a.add(4)
        self.a.add(5)
        self.assertEqual(self.a.remove(), 2)

    def test_remove_four(self):
        self.a.add(1)
        self.a.add(2)
        self.a.remove()
        self.a.add(3)
        self.a.remove()
        self.a.add(4)
        self.a.add(5)
        self.a.remove()
        self.assertEqual(self.a.remove(), 4)

    def test_peek_one(self):
        self.a.add(1)
        self.assertEqual(self.a.peek(), 1)

    def test_peek_two(self):
        self.a.add(1)
        self.a.add(2)
        self.assertEqual(self.a.peek(), 1)

    def test_peek_three(self):
        self.a.add(1)
        self.a.add(2)
        self.a.remove()
        self.a.add(3)
        self.a.remove()
        self.a.add(4)
        self.a.add(5)
        self.a.remove()
        self.assertEqual(self.a.peek(), 4)

class TestSortStack(unittest.TestCase):
    pass 


class TestAnimalShelter(unittest.TestCase):
    pass 

if __name__ == '__main__':
    unittest.main()