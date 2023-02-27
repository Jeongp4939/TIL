# https://www.cs.usfca.edu/~galles/visualization/RedBlack.html

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root

        while True:
            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right

    def find_min(self):
        current_node = self.root

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.key

    def find_max(self):
        current_node = self.root

        while current_node.right is not None:
            current_node = current_node.right

        return current_node.key

    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, node, key):
        if node is None:
            return None

        if key == node.key:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            min_node = self._find_min_node(node.right)
            node.key = min_node.key
            node.right = self._remove_recursive(node.right, min_node.key)

        elif key < node.key:
            node.left = self._remove_recursive(node.left, key)
        else:
            node.right = self._remove_recursive(node.right, key)

        return node

    def _find_min_node(self, node):
        current_node = node

        while current_node.left is not None:
            current_node = current_node.left

        return
