from binary_search_tree import BinarySearchTree

if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(61)
    binary_search_tree.insert(89)
    binary_search_tree.insert(100)
    binary_search_tree.insert(90)
    binary_search_tree.insert(66)
    binary_search_tree.insert(43)
    binary_search_tree.insert(51)
    binary_search_tree.insert(16)
    binary_search_tree.insert(55)
    binary_search_tree.insert(11)
    binary_search_tree.insert(79)
    binary_search_tree.insert(77)
    binary_search_tree.insert(82)
    binary_search_tree.insert(32)

    print('Inorder Traversal')
    binary_search_tree.inorder_traversal()
    print()
    print('----------')

    print('Postorder Traversal')
    binary_search_tree.postorder_traversal()
    print()
    print('----------')

    print('Levelorder Traversal')
    binary_search_tree.levelorder_traversal()
    print()
    print('----------')

    print('Resultado da busca:', binary_search_tree.search(55).root)
    print('Resultado da busca:', binary_search_tree.search(30).root)

    print('O menor valor é', binary_search_tree.get_lowest_value())
    print('O maior valor é', binary_search_tree.get_highest_value())

    binary_search_tree.remove(55)
    binary_search_tree.remove(90)

    print('----------')
    print('Levelorder Traversal')
    binary_search_tree.levelorder_traversal()
    print()
    print('----------')
