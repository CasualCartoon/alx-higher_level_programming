#!/usr/bin/python3
"""Module for singly linked list"""


class Node:
    """Class representing a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node.

        Args:
            data (int): The data for the node.
            next_node (Node, optional): The next node in the list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or if next_node is not None or a Node.
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
            value (int): The data to set.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If next_node is not None or a Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class representing a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value of the new Node.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Convert the linked list to a string representation."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result


# Example usage:
# linked_list = SinglyLinkedList()
# linked_list.sorted_insert(5)
# linked_list.sorted_insert(2)
# linked_list.sorted_insert(8)
# print(linked_list)
