"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

import sys
sys.path.append('..')

from lambda_queue.queue import Queue
from stack.stack import Stack
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

    def __str__(self):
        return f'{self.value}'

    # Insert the given value into the tree
    def insert(self, value):
        tree_node = BSTNode(value)
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = tree_node
        
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = tree_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        if target < self.value:
            # check left side of tree
            if self.left is None:
                return False
            return self.left.contains(target)
        
        if target > self.value:
            # check right side of tree
            if self.right is None:
                return False
            return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # continuously traverse self.right until None
        if not self.right:
            return self.value
        return self.right.get_max()
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call fn on self.value
        fn(self.value)

        if self.right:
            self.right.for_each(fn)

        if self.left:
            self.left.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self): # removed node param
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)
        while len(queue):
            bst_node = queue.dequeue()
            print(bst_node.data.value)
            if bst_node.data.left:
                queue.enqueue(bst_node.data.left)
            if bst_node.data.right:
                queue.enqueue(bst_node.data.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()
        stack.push(self)
        while len(stack):
            bst_node = stack.pop()
            print(bst_node.data.value)
            if bst_node.data.left:
                stack.push(bst_node.data.left)
            if bst_node.data.right:
                stack.push(bst_node.data.right)
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.dft_print()