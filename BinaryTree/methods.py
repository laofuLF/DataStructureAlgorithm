class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        if self.root != None:
            return self._contains(value, self.root)
        else:
            return False

    def _contains(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._contains(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._contains(value, cur_node.right_child)
        return False

    def add(self, value):
        if self.contains(value):
            return False
        else:
            if self.root == None:
                self.root = Node(value)
            else:
                self.add_help(value, self.root)
            return True

    def add_help(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self.add_help(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self.add_help(value, cur_node.right_child)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left_child) + self.size(node.right_child)
