"""Takes in a deck of cards and sorts them by value."""


def sort_cards(cards):
    """Sorts a deck of cards by their value, with Aces low."""
    rank = {"A": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7,
            "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12}
    return sorted(cards, key=lambda x: rank[x])
