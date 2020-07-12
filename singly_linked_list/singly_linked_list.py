class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # supposed to be a node

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def remove_next(self):
        self.next = None

    def __str__(self):
        return f"{self.data}"

    def __eq__(self, value):
        return self.data == value

    def __gt__(self, node):
        return self.data > node.data


class LinkedList:
    def __init__(self, start=None):
        self.__tail = start
        self.__head = start
        self.length = 1 if start else 0

    def __len__(self):
        return self.length
        
    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, data=None):
        # honestly this is probably only for setting head initially
        if data is None: 
            pass
        node = data

        # if self.__head:
        #     # there's a head already
        #     self.__head.set_next(node)
        # print(f'new head: {node}')
        self.__head = node

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, data=None):
        if data is None:
            pass

        node =data

        if self.__tail is None:
            self.__tail = node
            return

        if self.head == self.tail:
            self.head.set_next(node)
            self.__tail = node
            return
        # when tail already exists do the following
        # this should connect the tail to the next node
        self.__tail.set_next(node)
        self.__tail = node

    def append(self, data):
        """
        Adds a new node to the tail or self.length + 1, sets a pointer from previous tail to next tail
        """
        # adds to tail
        node = Node(data) if data else data

        # case 1: no data
        if self.tail is None and self.head is None:
            self.head = node

        # case 2: data present / nodes exist
        self.tail = node
        self.add_length(1)

    def pop(self):
        """
        Removes current head or position 0 from the linked list if there is one present
        """
        # case 1: no data
        # case 2: 1 item
        # case 3: 2 items
        # case 3: 3+ items
        if self.tail is None and self.head is None:
            return None
        
        popped_node = self.head
        self.add_length(-1)
        if (self.tail and self.head) and (self.tail is self.head):
            self.head = None
            self.tail = None
            return popped_node
        
        if self.head.get_next() is self.tail:
            self.head = self.tail
            return popped_node

        self.head = self.head.get_next()
        return popped_node

        

    def traverse(self):
        node = self.head
        while node:
            node = node.get_next()


    def get_max(self):
        high = self.head
        node = self.head
        while node:
            high = node if node > high else high
            node = node.get_next()
        return high

    def add_length(self, number):
        self.length += number

    def stack_pop(self):
        """
        Removes the newest item added to the list or position self.length
        """

        # if no items present
        if self.length == 0:
            pass
        
        node = self.head
        while node:
            popped_node = self.tail
            
            if node.get_next() is None:
                # this is where there's only 1 item
                self.tail = None
                self.head = None
                self.add_length(-1)
                return popped_node
            else:
                # when there's 2+ items
                # we're on the first item and there is another item
                # need to check if the second next item is present
                if node.get_next().get_next() is None:
                    # basically, we just check one extra ahead 
                    # we remove the connection to the next 
                    node.remove_next()

                    self.tail = node
                    self.add_length(-1)
                    return popped_node
                node = node.get_next()


