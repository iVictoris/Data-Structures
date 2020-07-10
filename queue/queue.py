"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
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

new in, old out
"""
class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
    
    def __len__(self):
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass