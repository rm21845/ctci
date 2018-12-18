import unittest
from ctci.structs.linkedlist import LinkedList, SinglyLinkedList
from ctci.chapter2 import delmidnode, intersection, loopdetect, palindrome, partition, returnkthtolast, \
    rmdups, sumlists


class TestDelMidNode(unittest.TestCase):
    pass 

class TestIntersection(unittest.TestCase):
    pass 

class TestLoopDetect(unittest.TestCase):
    pass 

class Testpalindrome(unittest.TestCase):
    pass 

class TestPartition(unittest.TestCase):
    pass 

class TestReturnKthToLast(unittest.TestCase):

    def setUp(self):
        self.a = LinkedList()

    def test_zero(self):
        self.a.insert(1)
        self.assertEqual(returnkthtolast.find(self.a, 0), 1)

    def test_one(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(3)
        self.assertEqual(returnkthtolast.find(self.a, 1), 2)

    def test_two(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(4)
        self.a.insert(5)
        self.a.insert(78)
        self.a.insert(34)
        self.a.insert(54)
        self.a.insert(12)
        self.a.insert(90)
        self.a.insert(75)
        self.a.insert(10)
        self.assertEqual(returnkthtolast.find(self.a, 6), 54)

class TestRmTableDups(unittest.TestCase):
    
    def setUp(self):
        self.a = SinglyLinkedList()

    def test_table_no_dup(self):
        self.a.insert(4)
        self.a.insert(2)
        self.a.insert(3)
        rmdups.remove_with_table(self.a)

    def test_table_one_dup(self):
        self.a.insert(3)
        self.a.insert(2)
        self.a.insert(6)
        self.a.insert(2)
        self.a.insert(1)

        rmdups.remove_with_table(self.a)
        self.a.delete(2)
        self.assertEqual(self.a.search(2), None)

    def test_table_multi_dup(self):
        self.a.insert(3)
        self.a.insert(2)
        self.a.insert(6)
        self.a.insert(2)
        self.a.insert(1)
        self.a.insert(1)

        rmdups.remove_with_table(self.a)
        self.a.delete(2)
        self.a.delete(1)
        self.assertEqual(self.a.search(2), None)
        self.assertEqual(self.a.search(1), None)

    def test_table_edge_dup(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(6)
        self.a.insert(2)
        self.a.insert(1)
        self.a.insert(1)

        rmdups.remove_with_table(self.a)
        self.a.delete(2)
        self.a.delete(1)
        self.assertEqual(self.a.search(2), None)
        self.assertEqual(self.a.search(1), None)


class TestRmSortDups(unittest.TestCase):
    
    def setUp(self):
        self.a = SinglyLinkedList()

    def test_table_one_dup(self):
        self.a.insert(3)
        self.a.insert(2)
        self.a.insert(6)
        self.a.insert(2)
        self.a.insert(1)

        rmdups.remove_with_sort(self.a)
        self.a.delete(2)
        self.assertEqual(self.a.search(2), None)

    def test_table_multi_dup(self):
        self.a.insert(3)
        self.a.insert(2)
        self.a.insert(6)
        self.a.insert(2)
        self.a.insert(1)
        self.a.insert(1)

        rmdups.remove_with_table(self.a)
        self.a.delete(2)
        self.a.delete(1)
        self.assertEqual(self.a.search(2), None)
        self.assertEqual(self.a.search(1), None)

    def test_table_edge_dup(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(6)
        self.a.insert(2)
        self.a.insert(1)
        self.a.insert(1)

        rmdups.remove_with_table(self.a)
        self.a.delete(2)
        self.a.delete(1)
        self.assertEqual(self.a.search(2), None)
        self.assertEqual(self.a.search(1), None)

class TestSumLists(unittest.TestCase):
    
    def setUp(self):
        self.a = SinglyLinkedList()
        self.b = SinglyLinkedList()

    def test_same_length(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(3)
        self.b.insert(3)
        self.b.insert(2)
        self.b.insert(1)
        self.a = sumlists.sum(self.a, self.b)
        
        self.c = [4, 4, 4]
        self.d = list()
        for node in self.a:
            self.d.append(node.value)
        self.assertListEqual(self.c, self.d)
       

    def test_remainders(self):
        self.a.insert(6)
        self.a.insert(1)
        self.a.insert(7)

        self.b.insert(2)
        self.b.insert(9)
        self.b.insert(5)

        self.a = sumlists.sum(self.a, self.b)
        
        self.c = [2, 1, 9]
        self.d = list()
        for node in self.a:
            self.d.append(node.value)
        self.assertListEqual(self.c, self.d)

    def test_diff_length(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(3)

        self.b.insert(1)
        self.b.insert(3)
        self.b.insert(2)
        self.b.insert(1)
        self.a = sumlists.sum(self.a, self.b)
        
        self.c = [4, 4, 4, 1]
        self.d = list()
        for node in self.a:
            self.d.append(node.value)

        self.assertListEqual(self.c, self.d)


class TestFollowUpSumLists(unittest.TestCase):
    
    def setUp(self):
        self.a = SinglyLinkedList()
        self.b = SinglyLinkedList()

    def test_same_length(self):
        self.a.insert(1)
        self.a.insert(2)
        self.a.insert(3)
        self.b.insert(3)
        self.b.insert(2)
        self.b.insert(1)
        self.a = sumlists.follow_up(self.a, self.b)
        
        self.c = [4, 4, 4]
        self.d = list()
        for node in self.a:
            self.d.append(node.value)
        self.assertListEqual(self.c, self.d)
       

    def test_remainders(self):
        self.a.insert(7)
        self.a.insert(1)
        self.a.insert(6)

        self.b.insert(5)
        self.b.insert(9)
        self.b.insert(2)

        self.a = sumlists.follow_up(self.a, self.b)
        
        self.c = [9, 1, 2]
        self.d = list()
        for node in self.a:
            self.d.append(node.value)
        self.assertListEqual(self.c, self.d)

    def test_diff_length(self):
        self.a.insert(3)
        self.a.insert(2)
        self.a.insert(1)

        self.b.insert(1)
        self.b.insert(2)
        self.b.insert(3)
        self.b.insert(1)
        self.a = sumlists.follow_up(self.a, self.b)
        
        self.c = [1, 4, 4, 4]
        self.d = list()
        for node in self.a:
            self.d.append(node.value)

        self.assertListEqual(self.c, self.d)
    

if __name__ == '__main__':
    unittest.main()