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

    # Percurso em ordem simétrica
    def simetric_traversal(self, node=None):
        if not node:
            node = self.root

        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)

        print(node, end='')

        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')


if __name__ == "__main__":
    binary_tree = BinaryTree()
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

    binary_tree.root = n2
    binary_tree.simetric_traversal()
