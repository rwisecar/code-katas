"""An implementation of a trie for the autocomplete kata."""
from collections import OrderedDict


class TrieNode(object):
    """Create node to for use in a trie tree."""

    def __init__(self, value=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.children = OrderedDict()


class Trie(object):
    """An implementation of a trie tree.

    insert(self, string): will insert the input string into the trie. If character in the input string is already present, it will be ignored.

    contains(self, string): will return True if the string is in the trie, False if not.

    size(self): will return the total number of words contained within the trie. 0 if empty.

    remove(self, string): will remove the given string from the trie. If the word does not exist, will raise an appropriate exception.

    traversal(self, start): Perform a full depth-first traversal of the graph beginning at start. The argument start should be a string, which may or may not be the beginning of a string or strings contained in the Trie.
    """

    def __init__(self):
        """Initialize a trie tree."""
        self.root = TrieNode()
        self._size = 0

    def insert(self, string):
        """Insert a string into the trie."""
        if not isinstance(string, str):
            raise TypeError("Word must be a string")
        string = string.lower()
        current = self.root
        for letter in string:
            if letter in current.children:
                current = current.children[letter]
            else:
                current.children[letter] = TrieNode(letter)
                current = current.children[letter]
        if '$' not in current.children:
            current.children['$'] = string
            self._size += 1

    def contains(self, string):
        """Return true if string is in trie."""
        if not isinstance(string, str):
            raise TypeError("Word must be a string")
        current = self.root
        for letter in string:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        try:
            if current.children['$']:
                return True
        except KeyError:
            raise KeyError("That word has not been inserted")

    def size(self):
        """Return the number of words contained in the trie."""
        return self._size

    def remove(self, string):
        """Return the string from the trie if it exists."""
        if not isinstance(string, str):
            raise TypeError("Word must be a string")
        current = self.root
        last_bifurcated_node = None
        value_at_last_bifurcation = None
        for letter in string:
            if letter in current.children:
                if len(current.children) > 1:
                    last_bifurcated_node = current
                    value_at_last_bifurcation = letter
                current = current.children[letter]
        if '$' in current.children and len(current.children) == 1:
            if last_bifurcated_node:
                del last_bifurcated_node.children[value_at_last_bifurcation]
                self._size -= 1
            else:
                del self.root.children[string[:1]]
        elif len(current.children) > 1:
            del current.children['$']
        else:
            raise KeyError('Word is not in trie')

    def traversal(self, start=None):
        """Return a list of all the words in the subtree starting at start."""
        current = self.root
        if start:
            for letter in start:
                if letter in current.children:
                    current = current.children[letter]
                else:
                    return
        result = self._traversal(current, True)
        for val in result:
            yield val.value

    def _traversal(self, node, first=False):
        if not first:
            yield node
        for child in node.children:
            if child == '$':
                continue
            for val in self._traversal(node.children[child]):
                yield val
