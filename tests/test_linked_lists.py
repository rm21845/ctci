import unittest
from ctci.structs.linkedlist import Node, LinkedList, SinglyLinkedList, DoublyLinkedList


class TestNode(unittest.TestCase):

    def setUp(self):
        self.zero = Node(0)
        self.one = Node(1)
        self.two = Node(2)

    def test_value(self):
        self.assertEqual(self.zero.value, 0) 

    def test_next_node(self):
        self.zero.next_node = self.one
        self.assertEqual(self.zero.next_node, self.one)

    def test_prev_node(self):
        self.two.prev_node = self.one
        self.assertEqual(self.two.prev_node, self.one)


class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.a = LinkedList()

    def test_insert_zero(self):
        self.a.insert(0)
        self.assertEqual(self.a.head.value, 0)

    def test_insert_one(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(4)
        self.assertEqual(self.a.head.value, 4)
        
    def test_len_empty(self):
        
        self.assertEqual(len(self.a), 0)

    def test_len_one(self):
        self.a.insert(3)
        self.a.insert(2)
        
        self.assertEqual(len(self.a), 2)

    def test_len_two(self):
        self.a.insert(3)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        
        self.assertEqual(len(self.a), 6)

    def test_search_one(self):
        self.a.insert(44)
        found_node = self.a.search(44)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.value, 44)
        
    def test_search_two(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.insert(34)
        self.a.insert(78)
        found_node = self.a.search(78)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.value, 78)

    def test_search_three(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.insert(34)
        self.a.insert(78)
        found_node = self.a.search(67)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.value, 67)

    def test_search_no_exist(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.insert(34)
        self.a.insert(78)
        self.assertEqual(self.a.search(100), None)

    def test_delete_zero(self):
        self.a.insert(44)
        self.a.delete(44)
        self.assertEqual(self.a.search(66), None)
        
    def test_delete_one(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.delete(66)
        self.assertEqual(self.a.search(66), None)

    def test_delete_two(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.delete(67)
        self.assertEqual(self.a.search(67), None)


class TestSinglyLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.a = SinglyLinkedList()

    def test_len_empty(self):
        
        self.assertEqual(len(self.a), 0)

    def test_len_one(self):
        self.a.insert(3)
        self.a.insert(2)
        
        self.assertEqual(len(self.a), 2)

    def test_len_two(self):
        self.a.insert(3)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        
        self.assertEqual(len(self.a), 6)


    def test_insert_zero(self):
        self.a.insert(0)
        self.assertEqual(self.a.head.value, 0)

    def test_insert_one(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(4)
        self.assertEqual(self.a.head.value, 4)

    def test_search_one(self):
        self.a.insert(44)
        found_node = self.a.search(44)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.value, 44)
        
    def test_search_two(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.insert(34)
        self.a.insert(78)
        found_node = self.a.search(78)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.value, 78)

    def test_search_no_exist(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.insert(34)
        self.a.insert(78)
        self.assertEqual(self.a.search(100), None)

    def test_delete_zero(self):
        self.a.insert(44)
        self.a.delete(44)
        self.assertEqual(self.a.search(66), None)
        
    def test_delete_one(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.delete(66)
        self.assertEqual(self.a.search(66), None)

    def test_delete_two(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.delete(67)
        self.assertEqual(self.a.search(67), None)


class TestDoublyLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.a = DoublyLinkedList()

    def test_len_empty(self):
        
        self.assertEqual(len(self.a), 0)

    def test_len_one(self):
        self.a.insert(3)
        self.a.insert(2)
        
        self.assertEqual(len(self.a), 2)

    def test_len_two(self):
        self.a.insert(3)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        self.a.insert(2)
        
        self.assertEqual(len(self.a), 6)

    def test_insert_zero(self):
        self.a.insert(0)
        self.assertEqual(self.a.head.value, 0)

    def test_insert_one(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(4)
        self.assertEqual(self.a.head.value, 4)

    def test_search_one(self):
        self.a.insert(44)
        found_node = self.a.search(44)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.value, 44)
        
    def test_search_two(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.insert(34)
        self.a.insert(78)
        found_node = self.a.search(78)
        self.assertIsInstance(found_node, Node)
        self.assertEqual(found_node.value, 78)

    def test_search_no_exist(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.insert(34)
        self.a.insert(78)
        self.assertEqual(self.a.search(100), None)

    def test_delete_zero(self):
        self.a.insert(44)
        self.a.delete(44)
        self.assertEqual(self.a.search(66), None)
        
    def test_delete_one(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.delete(66)
        self.assertEqual(self.a.search(66), None)

    def test_delete_two(self):
        self.a.insert(44)
        self.a.insert(66)
        self.a.insert(67)
        self.a.delete(67)
        self.assertEqual(self.a.search(67), None)


if __name__ == '__main__':
    unittest.main()