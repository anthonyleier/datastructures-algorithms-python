from queue import Queue


ROOT = 'ROOT'


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, value=None, node=None):
        if node:
            self.root = node
        elif value:
            node = Node(value)
            self.root = node
        else:
            self.root = None

    # Percurso em ordem simétrica (InOrder)
    def inorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        if node.left:
            # print('(', end='')
            self.inorder_traversal(node.left)

        print(node, end=',')

        if node.right:
            self.inorder_traversal(node.right)
            # print(')', end='')

    # Percurso em Pós-Ordem (PostOrder)
    def postorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)

        print(node, end=',')

    def get_height(self, node=ROOT):
        if node == ROOT:
            node = self.root

        height_left = 0
        height_right = 0

        if node.left:
            height_left = self.get_height(node.left)

        if node.right:
            height_right = self.get_height(node.right)

        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

    # Percurso em ordem linha a linha
    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.add(node)
        while not queue.is_empty():
            node = queue.remove()

            if node:
                if node.left:
                    queue.add(node.left)
                if node.right:
                    queue.add(node.right)

                print(node, end=',')
