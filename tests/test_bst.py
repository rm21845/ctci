import unittest
from ctci.structs.bst import Node, Tree


class TestNode(unittest.TestCase):
    
    def setUp(self):
        self.a = Node(1)
        self.b = Node(2)

    def test_value(self):
        self.assertEqual(self.a.value, 1)

    def test_left(self):
        self.a.left = self.b
        self.assertEqual(self.a.left, self.b)

    def test_right(self):
        self.a.right = self.b
        self.assertEqual(self.a.right, self.b)

    def test_parent(self):
        self.a.parent = self.b
        self.assertEqual(self.a.parent, self.b)

    def test_is_leaf(self):
        self.assertTrue(self.a.is_leaf())

    def test_is_not_leaf(self):
        self.a.left = self.b 
        self.assertFalse(self.a.is_leaf())

    def test_has_parent(self):
        self.a.parent = self.b
        self.assertTrue(self.a.has_parent())

    def test_has_not_parent(self):
        self.assertFalse(self.a.has_parent())

class TestTree(unittest.TestCase):

    def setUp(self):
        self.a = Tree()
    
    def test_root_insert(self):
        self.a.insert(1)
        self.assertEqual(self.a.search(1).value, 1)

    def test_insert_one(self):
        self.a.insert(1)
        self.a.insert(2)
        self.assertEqual(self.a.search(2).value, 2)
    
    def test_insert_two(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(4)
        self.a.insert(54)
        self.a.insert(80)
        self.assertEqual(self.a.search(54).value, 54)

    def test_search_empty(self):
        self.assertEqual(self.a.search(20), None)  

    def test_not_search_(self):
        self.a.insert(2)
        self.a.insert(4)
        self.assertEqual(self.a.search(20), None)        
    
    def test_delete_root(self):
        self.a.insert(10)
        self.a.delete(10)
        self.assertEqual(self.a.search(10), None)        
    
    def test_delete_leaf(self):
        self.a.insert(2)
        self.a.insert(1)
        self.a.insert(3)
        self.a.delete(1)
        self.assertEqual(self.a.search(1), None)        

    def test_delete_one_child_left(self):
        self.a.insert(2)
        self.a.insert(1)
        self.a.delete(2)
        self.assertEqual(self.a.search(2), None)        

    def test_delete_one_child_right(self):
        self.a.insert(2)
        self.a.insert(3)
        self.a.delete(2)
        self.assertEqual(self.a.search(2), None)    

    def test_delete_one_child(self):
        self.a.insert(5)
        self.a.insert(4)
        self.a.insert(7)
        self.a.insert(2)
        self.a.delete(4)
        self.assertEqual(self.a.search(4), None)

    def test_delete_two_child(self):
        self.a.insert(5)
        self.a.insert(1)
        self.a.insert(10)
        self.a.delete(5)
        self.assertEqual(self.a.search(5), None)
        self.assertEqual(self.a.search(1).value, 1)
        self.assertEqual(self.a.search(10).value, 10)

    def test_minimum(self):
        self.a.insert(10)
        self.a.insert(23)
        self.a.insert(40)
        self.a.insert(7)
        self.a.insert(2)
        self.assertEqual(self.a.minimum().value, 2)

    def test_maximum(self):
        self.a.insert(10)
        self.a.insert(23)
        self.a.insert(40)
        self.a.insert(7)
        self.a.insert(2)
        self.assertEqual(self.a.maximum().value, 40)

class TestTraversals(unittest.TestCase):

    def setUp(self):
        self.a = Tree()
        self.a.insert(7)
        self.a.insert(4)
        self.a.insert(2)
        self.a.insert(6)
        self.a.insert(3)
        self.a.insert(5)
        self.a.insert(12)
        self.a.insert(9)
        self.a.insert(19)
        self.a.insert(8)
        self.a.insert(11)
        self.a.insert(15)
        self.a.insert(20)

    def test_in_order(self):
        print('\nIN_ORDER')
        self.a.in_order()

    def test_pre_order(self):
        print('\nPRE_ORDER')
        self.a.pre_order()

    def test_post_order(self):
        print('\nPOST_ORDER')
        self.a.post_order()

if __name__ == '__main__':
    unittest.main()

