# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 11-06-2022
# Description: A linked list that has recursive add, remove, contains, insert, and reverse and to_plain_list methods.

class Node:
    """
    Represents a node in a linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Represents the LinkedList class.
    """

    def __init__(self):
        self._head = None

    def get_head(self):
        """
        Get method for returnin g first Node in list.
        """
        return self._head

    def rec_add(self, val, curr):
        """
        Recursive add method. Adds node containing val to end of linked list.
        """
        if curr.next is None:
            curr.next = Node(val)
            return
        self.rec_add(val, curr.next)

    def add(self, val):
        """
        Recursive add helper method.
        """
        if self._head is None:
            self._head = Node(val)
            return
        curr = self._head
        self.rec_add(val, curr)

    def rec_remove(self, val, curr):
        """
        Recursive remove method for nodes containing val within linked list. Checks if list is empty and returns. Then
        checks if head should be removed and if so, makes head refer to next node.
        """
        if curr.next is None:
            return

        if curr.next.data == val:
            curr.next = curr.next.next
            return

        else:
            self.rec_remove(val, curr.next)

    def remove(self, val):
        """
        Recursive remove helper method.
        """

        if self._head is None:
            return

        if self._head.data == val:
            self._head = self._head.next
            return

        else:
            self.rec_remove(val, self._head)

    def rec_contains(self, val, curr):
        """
        Recursive contains method. Returns True if value is in linked list, otherwise returns False.
        """

        if curr is not None:
            if curr.data == val:
                return True
            return self.rec_contains(val, curr.next)

    def contains(self, val):
        """
        Recursive contains helper method.
        """
        if self._head is None:
            return False

        else:
            return self.rec_contains(val, self._head)

    def rec_insert(self, val, index, curr):
        """
        Recursive insert method. Adds node with to linked list based on position.
        """
        if index == 0:
            self._head = Node(val)

        if curr is None:
            return self._head

        else:
            self.rec_insert(val, index, curr)

    def insert(self, val, index):
        """
        Recursive insert helper method.
        """
        self.rec_insert(self._head, val, index)

    def rec_reverse(self, curr):
        """
        Recursive reverse method. Reverses the order of nodes in linked list.
        """

        if curr.next is not None:
            self.rec_reverse(curr.next)
        self._head = curr.next

    def reverse(self):
        """
        Recursive reverse helper method.
        """
        return self.rec_reverse(self._head)

    def rec_to_plain_list(self, curr, plain_list):
        """
        Recursive method that returns a regular Python list with the same values and order as current state of the
        linked list.
        """
        plain_list.append(curr.data)
        if curr.next is not None:
            self.rec_to_plain_list(curr.next, plain_list)
            return

    def to_plain_list(self):
        """
        Recursive to_plain_list helper method.
        """
        plain_list = []
        if self._head is None:
            return plain_list

        else:
            self.rec_to_plain_list(self._head, plain_list)
        return plain_list
