#!/usr/bin/python3
"""Define a class Node that defines a node of a singly linked list."""


class Node:
    """Represent a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data: The data to be stored in the node (an integer).
            next_node: The next node in the linked list (a Node object).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value: The data to be stored in the node (an integer).

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list.

        Args:
            value: The next node in the linked list (a Node object) or None.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order).

        Args:
            value: The data to be stored in the new Node (an integer).
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the singly linked list."""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
