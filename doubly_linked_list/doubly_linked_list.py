"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_next(self, node):
        # what if node had a previous node already
        # get rid of prev node's next aka set to None
        if node.prev:
            node.prev.next = None # cleans up previous node
        
        # afterwards we would set node.prev to this node or self
        # and then set this node's next to node or self.next = node
        node.prev = self
        self.next = node

    """
    Inserts a node to `this` node's prev property. Will update the pointers from all parties involved.
    Will unset the `node` ref's next's previous if there is one
    """
    def insert_previous(self, node):
        if node.next:
            node.next.prev = None # cleans up next node's previous pointer
        node.next = self
        self.prev = node

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def set_head_and_tail_to(self, node):
        self.head = node
        self.tail = node
        self.length = 1

    def reset(self):
        self.head = None
        self.tail = None
        self.length = 0

    def tail_is_heads(self):
        return self.tail is self.head

    def node_is_tails_or_head(self, node):
        return node is self.tail or node is self.head

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # case 1: linked list empty
        # case 2: linked list has 1+
        node = ListNode(value)
        if self.head is None and self.tail is None:
            # case 1
            self.set_head_and_tail_to(node)
        else:
            self.head.insert_previous(node)
            self.head = node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        head = self.head
        self.delete(self.head)
        return head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # case 1: linked list empty
        # case 2: linked list has 1+
        node = ListNode(value)
        if self.head is None and self.tail is None:
            # case 1
            self.set_head_and_tail_to(node)
        else:
            self.tail.insert_next(node)
            self.tail = node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        tail = self.tail
        self.delete(self.tail)
        return tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):

        # case 1: is empty or self.head do nothing
        # case 2: node == self.self
        # case 3: any node that isn't tails

        if node is None or node is self.head:
            return
        # if node is tail, new tail must be set
        elif node is self.tail:
            self.remove_from_tail()
        else:
            self.delete(node)
        value = node.value
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # case 1: is empty or self.tail do nothing
        # case 2: node == self.head
        # case 3: any node that isn't tails

        if node is None or node is self.tail:
            return
        # if node is head, new head must be set
        elif node is self.head:
            self.remove_from_head()
        else:
            self.delete(node)
        value = node.value
        self.add_to_tail(value)
        


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # tests are only deleting tail/heads so coding according to that otherwise we need an identifier
        # case 1: no items
        # case 1: only 1 item exists
        # case 2: 2 items exist
        # case 3: more than 2 items exist

        if not self.length: 
            return

        if self.tail_is_heads():
            self.reset()
            return

        if self.node_is_tails_or_head(node):
            # `connected_node1 will be the node that's 
            # connected to the node being deleted
            # guaranteed to be either self.tail or self.head
            # as long as neither are `None`
            # node.delete will sever all connections to node
            # then we set tail and heads to the connected node
            connected_node = node.prev or node.next
            
            if self.length == 2:
                self.set_head_and_tail_to(connected_node)
                return
            
            if node is self.tail:
                self.tail = connected_node
            else:
                self.head = connected_node
        self.length -= 1
        node.delete() 

    """Returns the highest value currently in the list"""

    def get_max(self):
        high = self.head.value
        node = self.head

        while node:
            high = node.value if node.value > high else high
            node = node.next
        return high

