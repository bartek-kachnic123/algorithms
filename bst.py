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

    def rotate_right(self, subtree):
        # if subtree is None or subtree.left is None:
        #     return
        subtree.data, subtree.left.data = subtree.left.data, subtree.data
        tmp = subtree.left
        subtree.left = tmp.left
        tmp.left = tmp.right
        tmp.right = subtree.right
        subtree.right = tmp

    def rotate_left(self, subtree):
        tmp = subtree.right
        subtree.right = tmp.right
        tmp.right = tmp.left
        tmp.left = subtree.left

        subtree.data, subtree.right.data = subtree.right.data, subtree.data

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

    def bstToVine(self, grand):
        count = 0

        # Make tmp pointer to traverse and right flatten the given BST
        tmp = grand.right

        # while tmp is not null
        while tmp:

            # If left exist for node pointed by tmp then right rotate it
            if tmp.left:
                oldTmp = tmp
                tmp = tmp.left
                oldTmp.left = tmp.right
                tmp.right = oldTmp
                grand.right = tmp

            # If left dont exists add 1 to count and traverse further right to flatten remaining BST
            else:
                count += 1
                grand = tmp
                tmp = tmp.right

        return count
    def balanceBST(self):
        # create dummy node with value 0
        grand = Node(0)

        # assign the right of dummy node as our input BST
        grand.right = self.root

        # count = self.bstToVine(grand)
        count = self.tree_to_linkedList(grand.right)
        self.printPreorder(grand.right)
        # get the height of tree in which all levels are completely filled
        h = int(math.log2(count + 1))

        # get number of nodes until second last level
        m = pow(2, h) - 1

        # left rotate for excess nodes at last level
        self.compress(grand, count - m)

        # left rotate till m becomes 0
        # Steps is done as mentioned in algorithm to make BST balanced.
        for m in [m // 2 ** i for i in range(1, h + 1)]:
            self.compress(grand, m)

        self.root = grand.right
    def compress(self, grand, m: int):

        # Make tmp pointer to traverse and compress the given BST
        tmp = grand.right

        # Traverse and left-rotate root m times to compress given vine form of BST
        for i in range(m):
            oldTmp = tmp
            tmp = tmp.right
            grand.right = tmp
            oldTmp.right = tmp.left
            tmp.left = oldTmp
            grand = tmp
            tmp = tmp.right

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