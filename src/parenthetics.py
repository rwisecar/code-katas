"""Create a data structure that takes in a unicode string of parentheses,
and pushes it into a doubly linked list.
The balanced function checks whether each open paren in the list is matched.
If there is an unmatched open paren, the function will return 1.
If there is an unmatched closed paren, it will return -1.
If all parens are properly matched in the doubly linked list, it returns 0."""


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

    The balanced() function checks for three things.
    It returns 0 if each open paren is followed by a closed paren.
    It returns 1 if there is an unmatched open paren.
    It returns -1 if there is an unmatched closed paren."""

    def __init__(self, iterable=None):
        """Create an instance of a doubly linked list."""
        self._length = 0
        self.head = None
        self.tail = None

        if iterable:
            for value in iterable:
                self.push(value)
        elif iterable:
            raise TypeError

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

    def balanced(self):
        """Return 0 if equal number of matching open and closed parens.
        Return 1 if there is an open, unmatched, paren.
        Return -1 if there is an unmatched closed paren."""

        paren_dict = {'(': ')', ')': '('}

        if self.head:
            current = self.head
            if current.value == ')':
                return -1
            elif current.value == '(':
                while current:
                    if current == self.tail:
                        if current == ')':
                            return 0
                        elif current == '(':
                            return 1
                    elif current.next_node.value != paren_dict[current.value]:
                        if current.value == '(':
                            return 1
                        return -1
                    current = current.next_node
                return 0
            else:
                raise ValueError("Value not in list.")
        else:
            raise ValueError("Cannot balance an empty list.")
