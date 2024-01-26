import math
import collections
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

    def printInorder(self):
        self.inorder(self.root)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" "),
            self.inorder(root.right)

    def printPreorder(self):
        self.preorder(self.root)

    def preorder(self, root):
        if root:
            print(root.data, end=" "),
            self.preorder(root.left)
            self.preorder(root.right)

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
        while x != self.root and level > 0:
            x = x.parent
            level -= 1
        return x

    def inorder_g(self):
        current = self.root
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

    def _bstToVine(self, pseudo_root):
        count = 0
        node = pseudo_root.right

        while node:
            if node.left:

                temp = node.left
                node.left = temp.right
                if temp.right:
                    temp.right.parent = node
                temp.right = node
                node.parent = temp
                node = temp
                pseudo_root.right = temp
            else:
                count += 1
                pseudo_root = node
                node = node.right

        return count


    def balanceBST(self):
        pseudo_root = Node(0, right=self.root)
        count = self._bstToVine(pseudo_root)

        h = int(math.log2(count + 1))
        m = pow(2, h) - 1

        leaves = count - m
        self._compress(pseudo_root, leaves)
        count = count - leaves
        while count > 1:
            count = count // 2
            self._compress(pseudo_root, count)

        self.root = pseudo_root.right
        self.root.parent = None
        pseudo_root.right = None

    def _compress(self, pseudo_root, n):
        node = pseudo_root
        for i in range(n):
            child = node.right
            node.right = child.right
            if child.right:
                child.right.parent = node

            node = node.right
            child.right = node.left
            if node.left:
                node.left.parent = child

            node.left = child
            child.parent = node

    def height(self):
        maxh = 0
        queue = collections.deque()
        if self.root is None:
            return maxh

        queue.append((self.root, 1))

        while len(queue) > 0:
            item = queue.popleft()
            node = item[0]
            h = item[1]
            if node.left is not None:
                queue.append((node.left, h + 1))
            if node.right is not None:
                queue.append((node.right, h + 1))

            maxh = max(maxh, h)
        return maxh

    def draw(self):
        self._draw(self.root, level=0)

    def _draw(self, node, level):
        if node is None:
            return

        self._draw(node.right, level + 1)
        print("{}---{}".format("   |" * level, node.data))
        self._draw(node.left, level + 1)
