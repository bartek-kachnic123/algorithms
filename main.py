import bst


def test_balanaceBST(numbers):
    tree = bst.BinarySearchTree()
    for num in numbers:
        tree.insert(num)

    tree.draw()
    print(f"Wysokość drzewa przed zrównoważeniem = {tree.height()}")
    print()
    tree.balanceBST()
    tree.draw()
    print(f"Wysokość drzewa po zrównoważenieniu = {tree.height()}")


def main():
    test_balanaceBST([1, 3, 5, 2, 10, 11, 40, 23, 15])
    print()
    test_balanaceBST([i for i in range(1, 10)])


if __name__ == '__main__':
    main()


