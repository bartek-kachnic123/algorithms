import math
class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def isEmpty(self):
        return self.root is None

    def travel(self):
        self.printInorder(self.root)

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data, end=" "),
            self.printInorder(root.right)

    def travel2(self):
        self.printPreorder(self.root)


    def printPreorder(self, root):
        if root:
            print(root.data, end=" "),
            self.printPreorder(root.left)
            self.printPreorder(root.right)

    def search(self, data):
        current = self.root

        while current is not None:
            if current.data == data:
                return current
            elif current.data > data:
                current = current.left
            else:
                current = current.right
        return None

    def clear(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        current = self.root
        parent = None
        while current is not None:
            parent = current
            if current.data > data:
                current = current.left
            else:
                current = current.right
        if self.isEmpty():
            self.root = node
        elif parent.data > data:
            parent.left = node
        else:
            parent.right = node

        node.parent = parent
        return node

    def remove(self, data):
        node = self.search(data)

        if node is not None:
            parent = node.parent
            if node == self.root:
                self.root = self._remove(node)
                if self.root is not None:
                    self.root.parent = None
            elif parent.left == node:
                parent.left = self._remove(node)
                if parent.left is not None:
                    parent.left.parent = parent
            else:
                parent.right = self._remove(node)
                if parent.right is not None:
                    parent.right.parent = parent
            node.parent = None
        return node


    def _remove(self, node):
        if node.right is None:
            new_root = node.left
        elif node.left is None:
            new_root = node.right
        else:
            new_root = node
            node = node.left
            while node.right is not None:
                node = node.right
            node.right = new_root.right
            node = new_root
            new_root = node.left
        return new_root

    def travelUp(self, node, level=1):
        x = node
        while x != self.root and level != 0:
            x = x.parent
            level -= 1
        return x

    def dsw_balance(self):
        self.tree_to_linkedList(self.root)

    # def rotate_right(self, subtree):
    #     # if subtree is None or subtree.left is None:
    #     #     return
    #     subtree.data, subtree.left.data = subtree.left.data, subtree.data
    #     tmp = subtree.left
    #     subtree.left = tmp.left
    #     tmp.left = tmp.right
    #     tmp.right = subtree.right
    #     subtree.right = tmp
    #
    # def rotate_left(self, subtree):
    #     tmp = subtree.right
    #     subtree.right = tmp.right
    #     tmp.right = tmp.left
    #     tmp.left = subtree.left
    #
    #     subtree.data, subtree.right.data = subtree.right.data, subtree.data

    def tree_to_linkedList(self, root):
        node = root
        count = 0
        while node:
            while node.left:
                self.rotate_right(node)
            node = node.right
            count += 1

        if self.maxDepth(root) == count:
            print("Good")
        return count

    def bstToVine(self, pseudo_root):
        count = 0
        node = pseudo_root.right

        while node:
            # If left exist for node pointed by tmp then right rotate it
            if node.left:
                node = self.rotate_right(node)
                pseudo_root.right = node
            # If left dont exists add 1 to count and traverse further right to flatten remaining BST
            else:
                count += 1
                pseudo_root = node
                node = node.right

        return count

    def rotate_right(self, node):
        old_node = node
        node = node.left
        old_node.left = node.right

        if node.right:
            node.right.parent = old_node.left

        node.right = old_node

        old_node.parent = node.right

        return node

    def balanceBST(self):

        pseudo_root = Node(0, right=self.root)
        count = self.bstToVine(pseudo_root)

        self.printInorder(pseudo_root.right)
        # get the height of tree in which all levels are completely filled
        h = int(math.log2(count + 1))

        # get number of nodes until second last level
        m = pow(2, h) - 1

        # left rotate for excess nodes at last level
        self.compress(pseudo_root, count - m)

        # left rotate till m becomes 0
        # Steps is done as mentioned in algorithm to make BST balanced.
        for m in [m // 2 ** i for i in range(1, h + 1)]:
            self.compress(pseudo_root, m)

        self.root = pseudo_root.right
        pseudo_root.right = None


    def compress(self, pseudo_root, n):
        node = pseudo_root
        for i in range(n):
            child = node.right
            node.right = child.right
            child.right.parent = node.right

            node = node.right
            child.right = node.left

            if node.left:
                node.left.parent = child.right

            node.left = child
            child.parent = node

    def maxDepth(self, node):
        if node is None:
            return 0
        else:
            # Compute the depth of each subtree
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

            # Use the larger one
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1