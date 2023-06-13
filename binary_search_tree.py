from binary_tree import BinaryTree, Node


ROOT = 'ROOT'


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        pivot = self.root

        while (pivot):
            parent = pivot
            if value < pivot.value:
                pivot = pivot.left
            elif value > pivot.value:
                pivot = pivot.right

        if not parent:
            self.root = Node(value)
        elif value < parent.value:
            parent.left = Node(value)
        elif value > parent.value:
            parent.right = Node(value)

    def another_search(self, value):
        return self._another_search(value, self.root)

    def _another_search(self, value, node):
        if not node or node.value == value:
            return BinarySearchTree(node)

        if value < node.value:
            return self._another_search(value, node.left)

        if value > node.value:
            return self._another_search(value, node.right)

    def search(self, value, node=ROOT):
        if node == ROOT:
            node = self.root

        if not node or node.value == value:
            return BinarySearchTree(node)

        if value < node.value:
            return self.search(value, node.left)

        if value > node.value:
            return self.search(value, node.right)


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()
    binary_search_tree.insert(40)
    binary_search_tree.insert(30)
    binary_search_tree.insert(50)
    binary_search_tree.insert(33)
    binary_search_tree.insert(99)

    binary_search_tree.inorder_traversal()
    print()
    binary_search_tree.postorder_traversal()
    print()

    print('Buscando por 40:', binary_search_tree.search(40).root)
    print('Buscando por 30:', binary_search_tree.search(30).root)

    print('Buscando por 40:', binary_search_tree.another_search(40).root)
    print('Buscando por 30:', binary_search_tree.another_search(30).root)
