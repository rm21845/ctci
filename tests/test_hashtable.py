import unittest
from ctci.structs.hashtable import HashTable


class TestHashFunction(unittest.TestCase):
    def test_hash(self):
        expected = 16158402040730025812909810095587
        self.assertEqual(expected, HashTable.hash_fnv('4'))


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.a = HashTable()

    def test_zero(self):
        self.a.insert(1)
        self.assertEqual(self.a.search(1), 1)


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.a = HashTable()

    def test_zero(self):
        self.a.insert(1)
        self.a.insert(6)
        self.assertEqual(self.a.search(6), 6)

    def test_one(self):
        self.a.insert(1)
        self.a.insert(6)
        self.a.insert(8)
        self.a.insert(5)
        found = self.a.search(6)
        self.assertEqual(found, 6)

    def test_two(self):
        self.a.insert(1)
        self.a.insert(3)
        self.a.insert(6)
        self.assertEqual(self.a.search(1), 1)


class TestDelete(unittest.TestCase):
    def setUp(self):
        self.a = HashTable()

if __name__ == '__main__':
    unittest.main()