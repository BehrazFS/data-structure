class Node:
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, node, value):
        if node is None:
            return Node(value)
        if value <= node.data:
            node.left = self.__insert(node.left, value)
        elif value > node.data:
            node.right = self.__insert(node.right, value)
        return node

    def delete(self, value):
        self.root = self.__delete(self.root, value)

    def __delete(self, node, value):
        if node is None:
            return node
        if value < node.data:
            node.left = self.__delete(node.left, value)
        elif value > node.data:
            node.right = self.__delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.__find_min(node.right)
                node.data = temp.data
                node.right = self.__delete(node.right, temp.data)
        return node

    def __find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def get_lower_values(self, value):
        pass


bst = BinarySearchTree()
bst.insert(5)
bst.insert(2)
bst.insert(6)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(1)
bst.insert(19)
# bst.delete()
bst.in_order(bst.root)
