"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


"""
Let me make it easier to explain LIFO
Think of dishes

you stack them on top of each other
and remove them based on the top of each other

it's the last dish in that's the first dish out

vs FIFO

think of groceries
older is in the back
newer is in the front

employees stock new in the back
people buy items in the front

first <blank> in, first <blank> out
"""

import sys
sys.path.append('..')

from singly_linked_list.singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return (len(self.storage))


    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.stack_pop()
