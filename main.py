# This is a sample Python script.
import bst
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    tree = bst.BinarySearchTree()
    for i in range(1, 4):
        tree.insert(i)
    for i in range(10, 2, -1):
        tree.insert(i)

    node = tree.search(5)
    tree2 = bst.BinarySearchTree()
    tree2.insert(2)
    tree2.travel()
    tree2.remove(2)
    tree2.insert(5)
    tree2.insert(10)
    tree2.insert(5)
    tree2.insert(3)
    tree2.insert(4)
    tree2.insert(4)
    for i in range(-10, -4, 1):
        tree2.insert(i)
    print()
    tree2.travel()
    print()
    print(tree2.maxDepth(tree2.root))
    tree2.balanceBST()
    print()
    print(tree2.maxDepth(tree2.root))
    tree2.travel2()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
