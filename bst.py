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
        while x and x != self.root and level != 0:
            x = x.parent
            level -= 1
        return x

    def in_order(self):

        # Set current to root of binary tree
        current = self.root

        # Initialize stack
        stack = []

        while True:

            if current:
                stack.append(current)
                current = current.left

            elif stack:
                current = stack.pop()
                yield current.data
                current = current.right

            else:
                break

        print()

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
        for x in self._generate_iteration(m, h):
            self.compress(pseudo_root, x)

        # self.root = pseudo_root.right
        # self.root.parent = None
        pseudo_root.right = None

    def _generate_iteration(self, m, h):
        return (m // 2 ** i for i in range(1, h + 1))

    def compress(self, pseudo_root, n):
        node = pseudo_root
        for i in range(n):
            if node.right:
                child = node.right
                node.right = child.left
                if child.left:
                    child.left.parent = node
                child.parent = node.parent
                if node.parent is None:
                    self.root = child
                elif node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
                child.left = node
                node.parent = child

    def rotate_right(self, node):
        # old_node = node
        # node = node.left
        #
        # old_node.left = node.right
        # if node.right:
        #     node.right.parent = old_node.left
        #
        # node.right = old_node
        #
        # old_node.parent = node.right
        child = node.left
        node.left = child.right
        if child.right:
            child.right.parent = node
        child.parent = node.parent
        if node.parent is None:
            self.root = child
        elif node.parent.right == node:
            node.parent.right = child
        else:
            node.parent.left = child
        child.right = node
        node.parent = child

        return child

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