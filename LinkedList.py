# Author: Faith Elledge
# Githubuser: elledgef
# Date: 11/9/22
# Description: Code that uses recursive functions to add, remove and reverse the items in a Linked List. This code
# also uses recursive functions to insert items into a Linked List's index and also sees what this list contains.

class Node:

    def _init__(self, data):
        """node in a linked list"""
        self._data = data
        self._next = None

    class LinkedList:
        """ Linked List Class"""

    def __init__(self):
        self._head = None

    def get_head(self):
        """ Returns the """
        return self._head

    def rec_add(self, data, node):
        """ Recursive function that adds a new node"""
        if node is None:
            return self._head
        else:
            self.add(data)

    def add(self, val):
        """ Adds a new node to the linked list"""
        self._head = self.rec_add(self, val)

    def rec_remove(self, data, node):
        """ Recursive function that removes a node"""
        if node is None:
            return self._head
        if self._next(data) == data:
            return None
        elif self._next is None:
            pass
        else:
            self.remove(data)

    def remove(self, val):
        """Removes  node from the linked list"""
        self._head = self.rec_remove(self._head, val)

    def rec_contains(self, data, node=None):
        """ recursive function that indentifes if a node is contained within the Linked list"""
        if node is None:
            return False
        if self._data == data:
            return True
        else:
            self.contains(data)

    def contains(self, val):
        return self.rec_contains(self._head, val)

    def rec_insert(self, pos, node=None):
        """function to add to the index of a Linked List"""
        if node is None:
            return self._head
        elif pos == 0:
            return Node()
        else:
            self.insert()

    def insert(self):
        return self.rec_insert(self._head)

    def rec_reverse(self, node=None):
        """Recursive function that reverses the linked list"""
        if node is None:
            return node
        elif self._next is None:
            return node
        else:
            self.reverse()

    def reverse(self):
        return self.rec_reverse(self._head)

    def rec_display(self, a_node):
        """ recursive function to display the linked list """
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(self._head)

    def display(self):
        return self.rec_display(self._head)

    def rec_to_plain_list(self, node=None):
        """ recursive function that returns the normal list of items from a Linked List"""
        if node is None:
            return self._head
        if self._next is None:
            return []
        else:
            return [self._data] + self.to_plain_list()

    def to_plain_list(self):
        return self.to_plain_list()
