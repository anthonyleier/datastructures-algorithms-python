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

    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root

        if not node:
            return node

        if value < node.value:
            node.left = self.remove(value, node.left)
        elif value > node.value:
            node.right = self.remove(value, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                substitute = self.get_lowest_value(node.right)
                node.value = substitute
                node.right = self.remove(substitute, node.right)

        return node
