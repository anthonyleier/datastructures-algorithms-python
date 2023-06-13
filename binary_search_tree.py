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
    binary_search_tree.insert(61)
    binary_search_tree.insert(89)
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
