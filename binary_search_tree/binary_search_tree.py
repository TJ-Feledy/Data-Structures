import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare to current node
        # if no node
            # make new node (left or right) 
        # if smaller, go left
        if value < self.value:
            if self.left is None:
                # insert tree node
                self.left = BinarySearchTree(value)
            else:
                # continue to left
                self.left.insert(value)
        # if bigger, go right
        elif value > self.value:
            if self.right is None:
                # insert tree node
                self.right = BinarySearchTree(value)
            else:
                # continue right
                self.right.insert(value)
                

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare to current node
        # if smaller, go left
        # if bigger, go right
        # if equal, return true

        # if smaller, but can't go left, return false
        # if bigger, but can't go right, return false
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
