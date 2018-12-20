import unittest
from ctci.structs.stack import Stack
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
    
    def setUp(self):
        self.a = Stack()
        self.b = Stack()
        self.b.push(76)
        self.b.push(58)
        self.b.push(49)
        self.b.push(36)
        self.b.push(26)
        self.b.push(22)
        self.b.push(21)
        self.b.push(10)
        self.b.push(9)
        self.b.push(8)
        self.b.push(2)
        self.b.push(1)

    def test_one(self):
        self.a.push(1)
        self.a.push(22)
        self.a.push(8)
        self.a.push(10)
        self.a.push(26)
        self.a.push(58)
        self.a.push(21)
        self.a.push(36)
        self.a.push(9)
        self.a.push(49)
        self.a.push(2)
        self.a.push(76)

        self.a = sortstack.sort_stack(self.a)

        while not self.a.is_empty():
            self.assertTrue(self.a.pop() == self.b.pop())


class TestAnimalShelter(unittest.TestCase):
    
    def setUp(self):
        self.a = animalshelter.AnimalShelter()
        self.scar = animalshelter.Cat('Scar')
        self.nyla = animalshelter.Cat('Nyla')
        self.mufasa = animalshelter.Cat('Mufasa')
        self.simba = animalshelter.Cat('Simba')
        self.air_bud = animalshelter.Dog('AirBud')
        self.skip = animalshelter.Dog('Skip')
        self.clifford = animalshelter.Dog('Clifford')
        self.lassie = animalshelter.Dog('Lassie')

    def test_enqueue_dog(self):
        self.a.enqueue(self.lassie)
        self.assertEqual(self.a.dequeue_dog(), self.lassie)

    def test_enqueue_cat(self):
        self.a.enqueue(self.simba)
        self.assertEqual(self.a.dequeue_cat(), self.simba)

    def test_dequeue_cat(self):
        self.a.enqueue(self.scar)
        self.a.enqueue(self.nyla)
        self.a.enqueue(self.mufasa)
        self.a.enqueue(self.simba)
        self.assertEqual(self.a.dequeue_cat(), self.scar)

    def test_dequeue_dog(self):
        self.a.enqueue(self.air_bud)
        self.a.enqueue(self.skip)
        self.a.enqueue(self.clifford)
        self.a.enqueue(self.lassie)
        self.a.dequeue_dog()
        self.assertEqual(self.a.dequeue_dog(), self.skip)

    def test_dequeue(self):
        self.a.enqueue(self.air_bud)
        self.a.enqueue(self.nyla)
        self.a.enqueue(self.skip)
        self.a.enqueue(self.clifford)
        self.a.enqueue(self.lassie)
        self.a.enqueue(self.scar)
        self.a.enqueue(self.mufasa)
        self.a.enqueue(self.simba)
        self.assertEqual(self.a.dequeue(), self.air_bud)


if __name__ == '__main__':
    unittest.main()