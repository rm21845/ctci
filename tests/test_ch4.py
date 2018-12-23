import unittest
from ctci.structs.bst import Node
from ctci.chapter4 import bstsequences, buildorder, checkbalanced, checksubtree, firstcomancestor, \
    listofdepths, minimaltree, pathswithsum, randomnode, routebetweennodes, successor, validatebst


class TestBSTSequences(unittest.TestCase):

    def setUp(self):
        pass


class TestBuildOrder(unittest.TestCase):

    def setUp(self):
        pass


class TestCheckBalanced(unittest.TestCase):

    def test_height_two(self):
        node = Node(2)
        node.left = Node(1)
        node.right = Node(3)
        self.assertEqual(checkbalanced.height(node), 2)

    def test_is_balanced(self):
        node = Node(1)
        node.left = Node(2)
        node.right = Node(3)
        self.assertTrue(checkbalanced.is_balanced(node))

    def test_is_not_balanced(self):
        node = Node(1)
        node.left = Node(2)
        node.left.left = Node(3)
        self.assertFalse(checkbalanced.is_balanced(node))

class TestCheckSubTree(unittest.TestCase):

    def setUp(self):
        pass


class TestFirstComAncestor(unittest.TestCase):

    def setUp(self):
        pass


class TestListOfDepths(unittest.TestCase):

    def setUp(self):
        pass


class TestMinimalTree(unittest.TestCase):

    def setUp(self):
        self.a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_one(self):
        minimaltree.min_height(self.a) 


class TestPathsWithSum(unittest.TestCase):

    def setUp(self):
        pass


class TestRandomNode(unittest.TestCase):

    def setUp(self):
        pass


class TestRouteBetweenNodes(unittest.TestCase):

    def setUp(self):
        self.graph = [[1, 2], [6], [3, 4], [], [5], [], []]

    def test_route_true(self):
        self.assertTrue(routebetweennodes.is_route(self.graph, (0, 5)))

    def test_route_false(self):
        self.assertFalse(routebetweennodes.is_route(self.graph, (2, 6)))

class TestSuccessor(unittest.TestCase):

    def setUp(self):
        pass


class TestValidateBST(unittest.TestCase):

    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()
