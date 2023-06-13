from binary_tree import BinaryTree, Node, ROOT


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        pivot = self.root

        while (pivot):
            parent = pivot
            if value < pivot.value:
                pivot = pivot.left
            else:  # value > pivot.value
                pivot = pivot.right

        if not parent:
            self.root = Node(value)
        elif value < parent.value:
            parent.left = Node(value)
        else:  # value > parent.value
            parent.right = Node(value)

    def search(self, value, node=ROOT):
        if node == ROOT:
            node = self.root

        if not node or node.value == value:
            return BinarySearchTree(node)

        if value < node.value:
            return self.search(value, node.left)

        if value > node.value:
            return self.search(value, node.right)

    def get_lowest_value(self, node=ROOT):
        if node == ROOT:
            node = self.root

        if node.left:
            return self.get_lowest_value(node.left)
        else:
            return node

    def get_highest_value(self, node=ROOT):
        if node == ROOT:
            node = self.root

        if node.right:
            return self.get_highest_value(node.right)
        else:
            return node


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(33)
    binary_search_tree.insert(56)
    binary_search_tree.insert(12)
    binary_search_tree.insert(89)
    binary_search_tree.insert(27)
    binary_search_tree.insert(22)
    binary_search_tree.insert(22)

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

    print('Buscando por 33:', binary_search_tree.search(33).root)
    print('Buscando por 30:', binary_search_tree.search(30).root)

    print('O menor valor é', binary_search_tree.get_lowest_value())
    print('O maior valor é', binary_search_tree.get_highest_value())
