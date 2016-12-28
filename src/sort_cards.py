"""Takes in a deck of cards and sorts them by value."""


def sort_cards(cards):
    """Sorts a deck of cards by their value, with Aces low."""
    rank = {"A": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7,
            "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12}
    sorted_list = []
    for c in cards:
        sorted_list.append((c, rank[c]))
    sorted_list = [x[0] for x in sorted(sorted_list, key=lambda x: x[1])]
    return sorted_list
