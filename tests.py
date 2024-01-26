import unittest
from bst import BinarySearchTree as BinaryTree


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        # Create an initial binary tree for testing
        self.tree = BinaryTree()
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(20)

    def test_insert(self):
        self.assertTrue(self.tree.search(10))
        self.assertTrue(self.tree.search(5))
        self.assertTrue(self.tree.search(15))
        self.assertTrue(self.tree.search(3))
        self.assertTrue(self.tree.search(7))
        self.assertTrue(self.tree.search(20))
        self.assertFalse(self.tree.search(8))

    def test_remove_leaf_node(self):
        self.assertTrue(self.tree.search(3))
        self.tree.remove(3)
        self.assertFalse(self.tree.search(3))

    def test_remove_node_with_one_child(self):
        self.assertTrue(self.tree.search(15))
        self.tree.remove(15)
        self.assertFalse(self.tree.search(15))

    def test_remove_node_not_exists(self):
        self.tree.remove(100)

    def test_remove_node_with_two_children(self):
        self.assertTrue(self.tree.search(5))
        self.tree.remove(5)
        self.assertFalse(self.tree.search(5))

    def test_remove_nonexistent_node(self):
        result = self.tree.remove(8)
        self.assertIsNone(result)

    def test_travelUp_to_root(self):
        node = self.tree.search(5)
        result = self.tree.travelUp(node)
        self.assertEqual(result.data, 10)

    def test_travelUp_to_level(self):
        node = self.tree.search(3)
        result = self.tree.travelUp(node, level=2)
        self.assertEqual(result.data, 10)

    def test_travelUp_to_root_with_root_level(self):
        node = self.tree.search(15)
        result = self.tree.travelUp(node, level=0)
        self.assertEqual(result.data, 15)

    def test_balanceBST(self):
        tree = BinaryTree()
        for i in range(10, 3, -1):
            tree.insert(i)

        node = tree.search(9)
        result = tree.travelUp(node, 10)
        self.assertEqual(result.data, tree.root.data)
        tree.balanceBST()
        node2 = tree.search(10)
        node3 = tree.search(9)
        self.assertEqual(node2.parent.data,  node3.data)
        node4 = tree.travelUp(node3, 10)
        self.assertEqual(tree.root.data, node4.data)

    def test_travelUp_after_balance(self):
        numbers = [1, 3, 6, 4, 2, 5, 91, 123, 11, 12312, 1, 3, 234, 23432,2 , 22,22,11]
        tree = BinaryTree()
        for i in numbers:
            tree.insert(i)
        tree.balanceBST()
        h = tree.height()
        for num in numbers:
            node = tree.search(num)
            self.assertEqual(tree.travelUp(node, h).data, tree.root.data)

    def test_travelUp_after_balance2(self):
        numbers = [i for i in range(10, -10, -1)]
        tree = BinaryTree()
        for i in numbers:
            tree.insert(i)
        tree.balanceBST()
        h = tree.height()
        for num in numbers:
            node = tree.search(num)
            self.assertEqual(tree.travelUp(node, h).data, tree.root.data)

    def test_balanceBst(self):
        numbers = [1, 3, 6, 4, 2, 5, 91, 123, 11, 12312, 1, 3, 234, 23432, 2, 22, 22, 11]
        tree = BinaryTree()
        for i in numbers:
            tree.insert(i)
        before = tree.height()
        tree.balanceBST()
        after = tree.height()
        self.assertTrue(after < before)

if __name__ == '__main__':
    unittest.main()