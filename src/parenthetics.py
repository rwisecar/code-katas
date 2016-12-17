"""Create a data structure that takes in a unicode string of parentheses.
Check whether the last item is open '(', broken '))', or unbalanced.
A string is unbalanced if there is an unequal number of ')' and '('."""


class Node(object):
    """Create node to push into Doubly link list."""

    def __init__(self, value=None, next_node=None, previous_node=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


class DoubleLink(object):
    """Create a doubly linked list.

    The push() function adds new values to the list.

    The open() function checks whether the last value is an open paren.

    The broken() function checks whether the last two values are '))'.

    The balanced() function checks for an equal number of ')' and '('."""

    def __init__(self, head=None, iterable=None):
        """Create an instance of a doubly linked list."""
        self._length = 0
        self.head = None
        self.tail = None

        if iterable and hasattr(iterable, "__iter__"):
            for value in iterable:
                self.push(value)
        elif iterable:
            raise TypeError
        elif head and not iterable:
            self.push(head)

    def push(self, value):
        """Add new value to the front of a doubly linked list."""
        new_node = Node(value)
        if self.head:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self._length += 1