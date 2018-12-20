import unittest
from ctci.chapter4 import bstsequences, buildorder, checkbalanced, checksubtree, firstcomancestor, \
    listofdepths, minimaltree, pathswithsum, randomnode, routebetweennodes, successor, validatebst


class TestBSTSequences(unittest.TestCase):

    def setUp(self):
        pass


class TestBuildOrder(unittest.TestCase):

    def setUp(self):
        pass


class TestCheckBalanced(unittest.TestCase):

    def setUp(self):
        pass


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
        pass


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
