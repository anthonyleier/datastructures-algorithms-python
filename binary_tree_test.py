from binary_tree import BinaryTree, Node


def inorder_tree_test():
    inorder_tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    inorder_tree.root = n2

    print('Inorder Traversal')
    inorder_tree.inorder_traversal()
    print()
    print('----------')

    print('Postorder Traversal')
    inorder_tree.postorder_traversal()
    print()
    print('----------')

    print('Levelorder Traversal')
    inorder_tree.levelorder_traversal()
    print()
    print('----------')

    print('Altura:', inorder_tree.get_height())


def postorder_tree_test():
    postorder_tree = BinaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n11 = Node('-')
    n9 = Node('S')
    n10 = Node('E')

    n10.left = n6
    n10.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7
    n9.right = n11
    postorder_tree.root = n10

    print('Inorder Traversal')
    postorder_tree.inorder_traversal()
    print()
    print('----------')

    print('Postorder Traversal')
    postorder_tree.postorder_traversal()
    print()
    print('----------')

    print('Levelorder Traversal')
    postorder_tree.levelorder_traversal()
    print()
    print('----------')

    print('Altura:', postorder_tree.get_height())


if __name__ == "__main__":
    inorder_tree_test()
    postorder_tree_test()
