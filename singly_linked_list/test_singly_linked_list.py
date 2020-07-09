import unittest
from singly_linked_list import LinkedList
from singly_linked_list import Node

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()
    def test_node(self):
        node = Node(1)
        self.assertEqual(node, 1)
        node.set_next(Node(2))
        self.assertEqual(node.get_next(), 2)
        node.remove_next()
        self.assertEqual(node.get_next(), None)

    def test_append(self):
        self.list.append(1)
        self.assertEqual(self.list.head, 1)
        self.assertEqual(self.list.head.get_next(), None)
        self.assertEqual(self.list.tail, 1)
        self.list.append(2)
        self.assertEqual(self.list.head, 1)
        self.assertEqual(self.list.head.get_next(), 2)
        self.assertEqual(self.list.tail, 2)
        self.list.append(3)
        self.assertEqual(self.list.head.get_next().get_next(), 3)
        self.list.append(4)
        self.assertEqual(self.list.head.get_next().get_next().get_next(), 4)
        self.list.append(5)
        self.assertEqual(self.list.tail, 5)
        self.assertEqual(self.list.head, 1)
        


    def test_pop(self):
        self.assertEqual(self.list.pop(), 'LinkedList is empty')
        self.list.append(1)
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.pop(), 1)
        self.assertEqual(len(self.list), 0)
        self.list.append(2)
        self.assertEqual(self.list.head.data, 2)
        self.assertEqual(self.list.tail.data, 2)
        self.list.append(3)
        self.list.append(4)
        self.list.append(5)
        self.assertEqual(len(self.list), 4)
        self.list.pop()
        self.assertEqual(self.list.head, 3)
        self.assertEqual(self.list.tail.data, 5)

    def test_traverse(self):
        # h -> None <- t
        self.list.append(1)
        # h -> 1 <- t
        self.list.append(2)
        # h -> 1 -> 2 <- t
        self.list.append(3)
        # h -> 1 -> 2 -> 3 <- t
        self.list.traverse()
    def test_get_max(self):
        self.list.append(100)
        self.assertEqual(self.list.get_max(), 100)
        self.list.append(55)
        self.assertEqual(self.list.get_max(), 100)
        self.list.append(150)
        self.assertEqual(self.list.get_max(), 150)
        self.list.append(10)
        self.assertEqual(self.list.get_max(), 150)
        self.list.append(110)
        self.assertEqual(self.list.get_max(), 150)
        self.list.append(1000)
        self.assertEqual(self.list.get_max(), 1000)


    # screw these tests
    # def test_add_to_tail(self):
    #     self.list.add_to_tail(1)
    #     self.assertEqual(self.list.tail.value, 1)
    #     self.assertEqual(self.list.head.value, 1)
    #     self.list.add_to_tail(2)
    #     self.assertEqual(self.list.tail.value, 2)
    #     self.assertEqual(self.list.head.value, 1)

    # def test_contains(self):
    #     self.list.add_to_tail(1)
    #     self.list.add_to_tail(2)
    #     self.list.add_to_tail(5)
    #     self.list.add_to_tail(10)
    #     self.assertTrue(self.list.contains(10))
    #     self.assertTrue(self.list.contains(2))
    #     self.assertFalse(self.list.contains(1000))

    # def test_remove_head(self):
    #     self.list.add_to_tail(10)
    #     self.list.add_to_tail(20)
    #     self.assertEqual(self.list.remove_head(), 10)
    #     self.assertFalse(self.list.contains(10))
    #     self.assertEqual(self.list.remove_head(), 20)
    #     self.assertFalse(self.list.contains(20))

    #     self.list.add_to_tail(10)    
    #     self.assertEqual(self.list.remove_head(), 10)    
    #     self.assertIsNone(self.list.head)
    #     self.assertIsNone(self.list.tail)
    #     self.assertIsNone(self.list.remove_head())

    # def test_get_max(self):
    #     self.assertIsNone(self.list.get_max())
    #     self.list.add_to_tail(100)
    #     self.assertEqual(self.list.get_max(), 100)
    #     self.list.add_to_tail(55)
    #     self.assertEqual(self.list.get_max(), 100)
    #     self.list.add_to_tail(101)
    #     self.assertEqual(self.list.get_max(), 101)

if __name__ == '__main__':
    unittest.main()