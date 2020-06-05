#!/usr/bin/python3
"""Creating a Node class"""


class Node:
    """A node class for a linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The linked list class"""

    def __init__(self):
        self.head = None

    def __str__(self):
        linked_list = ''
        if self.head is None:
            return linked_list
        current_node = self.head
        while current_node is not None:
            if current_node.next_node is None:
                linked_list += str(current_node.data)
            else:
                linked_list += str(current_node.data) + '\n'
            current_node = current_node.next_node
        return linked_list

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        if current_node.data > new_node.data:
            new_node.next_node = current_node
            self.head = new_node
            return
        while current_node.next_node is not None and \
                new_node.data > current_node.next_node.data:
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node


sll = SinglyLinkedList()
print(sll)