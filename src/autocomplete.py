"""Take in an input string and a dictionary array.
Return the values from the dictionary that start with the input string.
Account for dictionary order and capitalization."""
from trietree import Trie


# def autocomplete(input_, dictionary):
#     """Code Wars kata autocomplete solution."""
#     return_arr = []
#     input_ = "".join([i for i in list(input_) if i.isalpha()])
#     for d in dictionary:
#         if d.lower().startswith(input_.lower()):
#             return_arr.append(d)
#     return return_arr[:5]


class Autocomplete(object):
    """
    Class based Autocomplete per class instructions.

    insert() adds a list of vocabulary words into the trie.

    autocomplete() traverses the trie and returns all words starting with the
    input string, limited by the number of max completions allowed by the user.
    """

    def __init__(self, vocabulary, max_completions=5):
        """Create a new trie instance."""
        self._trie = Trie()
        self.vocabulary = vocabulary
        self.max_completions = max_completions
        self.word_list = []

        for word in self.vocabulary:
            self._trie.insert(word)

    def autocomplete(self, start=None):
        """
        Return a list of words in the subtree starting with the input
        string. The list will be limited by the number of max completions.
        """
        self.word_list = []
        current = self._trie.root
        if start:
            for letter in start:
                if letter in current.children:
                    current = current.children[letter]
                else:
                    return
        self._autocomplete(current)
        return self.word_list[:self.max_completions]

    def _autocomplete(self, node):
        """Hidden method to traverse the trie."""
        if not node.children:
            return node
        for key, value in node.children.items():
            if key == '$':
                if value not in self.word_list:
                    self.word_list.append(value)
                else:
                    continue
            else:
                self._autocomplete(value)
        return self.word_list
