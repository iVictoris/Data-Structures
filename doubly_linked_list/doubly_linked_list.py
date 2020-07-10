"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

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

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # case 1: linked list empty
        # case 2: linked list has 1+
        node = ListNode(value)
        length_is_empty = not self.length
        if (length_is_empty):
            # case 1
            self.head = node
            self.tail = node

        # this is where list isn't empty
        current_head = self.head
        new_head = ListNode(value, current_head)
        self.head = new_head
        self.head.prev = current_head
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # case 1: empty list
        # case 2: list has len 1
        # case 3: longer than length of 1
        current_head = self.head
        list_is_empty = not self.length
        if (list_is_empty):
            pass
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            previous_head = current_head.prev
            self.head = previous_head
            previous_head.next = None
        self.length -= 1
        return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # case 1: linked list empty
        # case 2: linked list has 1+
        node = ListNode(value)
        length_is_empty = not self.length
        if (length_is_empty):
            # case 1
            self.head = node
            self.tail = node

        # this is where list isn't empty
        current_tail = self.tail
        new_tail = ListNode(value, current_tail)
        self.tail = new_tail
        self.tail.next = current_tail
        current_tail.prev = self.tail
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # case 1: empty list
        # case 2: list has len 1
        # case 3: longer than length of 1
        current_tail = self.tail
        list_is_empty = not self.length
        if (list_is_empty):
            pass
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            previous_tail = current_tail.next
            self.tail = previous_head
            previous_head.prev = None
        self.length -= 1
        return current_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):

        # case 1: is empty
        # case 2: node exists

        if (node is None):
            pass
        else:
            # pluck node out
            current_head = self.head
            previous_node, next_node = node.prev, node.next

            if previous_node and next_node:
                previous_node.next = next_node
                next_node.prev = previous_node

            if not previous_node:
                next_node.prev = None

            node.next = None
            current_head.next = node
            node.prev = current_head
            self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # case 1: is empty
        # case 3: node == self.head
        # case 2: node exists

        if (node is None):
            pass
        elif node == self.head:
            head = self.head  # old head
            tail = self.tail  # old tail
            self.head = head.prev
            self.head.next = None
            self.tail = head
            self.tail.next = tail
            tail.prev = self.tail
        else:
            # pluck node out
            current_tail = self.tail
            previous_node, next_node = node.prev, node.next

            if previous_node and next_node:
                previous_node.next = next_node
                next_node.prev = previous_node

            if not next_node:
                previous_node.next = None

            self.tail = node
            self.tail.prev = None
            current_tail.prev = self.tail
            self.tail.next = current_tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # tests are only deleting tail/heads so coding according to that otherwise we need an identifier
        # case 1: only 1 item exists
        if self.length == 1:
            self.head = None
            self.tail = None

        elif self.length == 2:

            if self.head == node:
                self.head = self.tail

            if self.tail == node:
                self.tail == self.head
        else:
            if self.head == node:
                previous_node = self.head.prev
                self.head = previous_node
                self.head.next = None

            if self.tail == node:
                previous_tail = self.tail.next
                self.tail = previous_tail
                self.tail.prev = None
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        node = self.tail
        value = node.value

        while (node):
            value = node.value if node.value > value else value
            node = node.next
        return value
