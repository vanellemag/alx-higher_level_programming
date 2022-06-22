#!/usr/bin/python3
"""100-singly_linked_list"""


class Node:
    """Class node that defines a node of a singly linked list"""

    def data(self):
        """property of private instance attribute"""
        self.__data

    def data(self, value):
        """setter"""
        try:
            if type(value) == int:
                self.__data = value
        except TypeError:
            raise TypeError('data must be an integer')

    def next_node(self):
        """retreive instance attribute"""
        self.__next_node

    def next_node(self, value):
        """setter"""
        try:
            self._next_node = Node()
            if value != "None":
                self.__next_node = value
        except TypeError:
            raise TypeError('next_node must be a Node object')

    def __init__(self, data, next_node=None):
        """instantiation"""
        self.__data = data
        self.__node_next = next_node


class SinglyLinkedList:
    """class that defines a singly lined list"""
    """__head """

    def __init__(self):
        """instantiation"""
        self.__head = Node()

    def sorted_insert(self, value):
        """instance method that insert a new Node"""
        while self.__head.data > value:
            self.__head = self.__head.next_node
        self.__head.data = value
