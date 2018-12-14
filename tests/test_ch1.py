import unittest
from ctci.chapter1 import unique, permutation, oneaway, palindrome, rotatematrix, \
    strcompression, strrotation, urlify, zeromatrix


class TestOneAway(unittest.TestCase):
    def test_empty(self):
        string_one = '' 
        string_two = '' 
        self.assertRaises(ValueError, lambda: oneaway.is_one_away(string_one, string_two))

    def test_zero_away(self):
        string_one = 'latex'
        string_two = 'latex'
        self.assertTrue(oneaway.is_one_away(string_one, string_two))

    def test_replace_positive(self):
        string_one = 'pale'
        string_two = 'bale'
        self.assertTrue(oneaway.is_one_away(string_one, string_two))

    def test_insert_positive(self):
        string_one = 'pale'
        string_two = 'ple'
        self.assertTrue(oneaway.is_one_away(string_one, string_two))

    def test_delete_positive(self):
        string_one = 'pales'
        string_two = 'pale'
        self.assertTrue(oneaway.is_one_away(string_one, string_two))

class TestPalindrome(unittest.TestCase):
    pass

class TestPermutation(unittest.TestCase):
    def test_empty(self):
        string_one = '' 
        string_two = '' 
        self.assertRaises(ValueError, lambda: permutation.check_perm(string_one, string_two))

    def test_is_perm(self):
        string_one = 'latex'
        string_two = 'exalt'
        self.assertTrue(permutation.check_perm(string_one, string_two))

    def test_not_perm(self):
        string_one = 'check'
        string_two = 'salty'
        self.assertFalse(permutation.check_perm(string_one, string_two))

    def test_diff_len(self):
        string_one = 'latex'
        string_two = 'exaltefef'
        self.assertFalse(permutation.check_perm(string_one, string_two))

class TestRotateMatrix(unittest.TestCase):
    pass

class TestStrCompression(unittest.TestCase):
    def test_empty(self):
        string = ''
        self.assertRaises(ValueError, lambda: strcompression.compress(string))

    def test_base(self):
        string = 'x'
        self.assertEqual('x1', strcompression.compress(string))

    def test_correct_one(self):
        string = 'aabcccccaaa'
        self.assertEqual('a2b1c5a3', strcompression.compress(string))

    def test_correct_two(self):
        string = 'aabbc'
        self.assertEqual('a2b2c1', strcompression.compress(string))

    def test_correct_three(self):
        string = 'aabcccccaaab'
        self.assertEqual('a2b1c5a3b1', strcompression.compress(string))


class TestStrRotation(unittest.TestCase):
    pass

class TestUnique(unittest.TestCase):
    
    def test_empty(self):
        string = ''
        self.assertRaises(ValueError, lambda: unique.is_unique(string))

    def test_unique(self):
        string = 'special'
        self.assertTrue(unique.is_unique(string))

    def test_not_unique(self):
        string = 'representation'
        self.assertFalse(unique.is_unique(string))

class TestURLify(unittest.TestCase):

    def test_empty(self):
        string = ''
        self.assertRaises(ValueError, lambda: urlify.to_url(string))

    #def test_whitespace_only(self):
     #   string = '      '
      #  self.assertEqual('%20', urlify.to_url(string))

    def test_correct(self):
        string = 'Mr John Smith      '
        self.assertEqual('Mr%20John%20Smith', urlify.to_url(string))

class TestZeroMatrix(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()