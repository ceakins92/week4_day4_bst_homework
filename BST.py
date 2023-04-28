# For tonight's assignment, you will create a decorator function that
# takes in a function as an argument. This decorator function will modify
# the behavior of the original function by converting a list input into a
# binary search tree. Here's what you need to do:
#
#
# Define a decorator function that takes in a function as an argument.Within the decorator function, define a wrapper function that takes in a list as an argument.Convert the input list into a #binary search tree.Pass the binary search tree as an argument to the original function.Return the result of the original function.

from Node import Node


class BinarySearchTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_node(self, value, node=None):
        if not node:
            node = self.root
        if value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                return self.add_node(value, node.right)
        else:
            if not node.left:
                node.left = Node(value)
                return
            else:
                return self.add_node(value, node.left)

    def get_min(self, node=None):
        if not node:
            node = self.root
        if node.left:
            return self.get_min(node.left)
        else:
            return node.value

    def get_max(self, node=None):
        if not node:
            node = self.root
        if node.right:
            return self.get_max(node.right)
        else:
            return node.value

    def get_max_loop(self, node=None):
        node = self.root
        while node.right:
            node = node.right
        return node.value

    def contains(self, target):
        current_node = self.root
        while current_node:
            if target == current_node.value:
                return True
            if target > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False

    def print_in_order(self, node=None):
        if not node:
            node = self.root
        if node.left:
            self.print_in_order(node.left)
        print(node.value)
        if node.right:
            self.print_in_order(node.right)

# ------Decorator Function
    def converter(func):
        # Wrapper
        def wrapper(alist):
            # Convert to tree
            bst = BinarySearchTree(alist[0])
            # add list items to tree as nodes
            for thing in alist:
                bst.add_node(thing)
            # Return results to original function
            result = func(bst)
            return result
        return wrapper

# -----Use Decorator
    @converter
    # Original Function
    def years(blist):
        return blist


history = BinarySearchTree.years([1979, 2001, 1786, 1492, 1984, 1999, 2022])

print(history.root.value)
print(history.get_min())
print(history.root.left.value)
print(history.root.right.value)
print(history.root.right.left.value)
print(history.get_max())
print(history.print_in_order())

# For tonight's assignment, you will create a decorator function that
# takes in a function as an argument. This decorator function will modify
# the behavior of the original function by converting a list input into a
# binary search tree. Here's what you need to do:
#
#
# Define a decorator function that takes in a function as an argument.Within the decorator function, define a wrapper function that takes in a list as an argument.Convert the input list into a #binary search tree.Pass the binary search tree as an argument to the original function.Return the result of the original function.
