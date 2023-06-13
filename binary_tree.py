class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, value=None):
        if value:
            node = Node(value)
            self.root = node
        else:
            self.root = None

    # Percurso em ordem simétrica (InOrder)
    def inorder_traversal(self, node=None):
        if not node:
            node = self.root

        if node.left:
            # print('(', end='')
            self.inorder_traversal(node.left)

        print(node, end='')

        if node.right:
            self.inorder_traversal(node.right)
            # print(')', end='')

    # Percurso em Pós-Ordem (PostOrder)
    def postorder_traversal(self, node=None):
        if not node:
            node = self.root

        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)

        print(node, end='')


if __name__ == "__main__":
    # InOrder
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
    inorder_tree.inorder_traversal()

    print()
    # PostOrder
    postorder_tree = BinaryTree()
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')
    n7 = Node('G')
    n8 = Node('H')
    n9 = Node('I')
    n0 = Node('J')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    postorder_tree.root = n0
    postorder_tree.postorder_traversal()
