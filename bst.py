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

    def is_empty(self):
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
        if self.is_empty():
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
        return x if x else self.root

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

    def _bstToVine(self, pseudo_root):
        count = 0
        node = pseudo_root.right

        while node:
            if node.left:
                node = self.rotate_right(node)
                pseudo_root.right = node
            else:
                count += 1
                pseudo_root = node
                node = node.right

        return count


    def balanceBST(self):
        grand = Node(0, right=self.root)
        count = self._bstToVine(grand)

        h = int(math.log2(count + 1))
        m = pow(2, h) - 1

        self._compress(grand, count - m)

        for x in self._generate_iteration(m, h):
            self._compress(grand, x)

        self.root = grand.right
        self.root.parent = None
        grand.right = None

    def _generate_iteration(self, m, h):
        return (m // 2 ** i for i in range(1, h + 1))

    def _compress(self, pseudo_root, n):
        scanner = pseudo_root
        for i in range(n):
            child = scanner.right
            scanner.right = child.right
            if child.right:
                child.right.parent = scanner

            scanner = scanner.right
            child.right = scanner.left
            if scanner.left:
                scanner.left.parent = child

            scanner.left = child
            child.parent = scanner
    def rotate_right(self, node):
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

    def treeHeight(self):

        # Base Case
        if self.root is None:
            return 0

        # Create a empty queue for level order traversal
        q = []

        # Enqueue Root and Initialize Height
        q.append(self.root)
        height = 0

        while (True):

            # nodeCount(queue size) indicates number of nodes
            # at current level
            nodeCount = len(q)
            if nodeCount == 0:
                return height

            height += 1

            # Dequeue all nodes of current level and Enqueue
            # all nodes of next level
            while (nodeCount > 0):
                node = q[0]
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                nodeCount -= 1