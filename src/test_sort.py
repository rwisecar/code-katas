"""Tests for sort-cards.py taken from codewars.com."""

from random import randint, choice
import pytest


SORTED_CARDS = 'A23456789TJQK'
TEST_CARDS = [
    'A', '3', 'T', 'T824Q', 'QKJ6932', 'J69327A8', 'J679J7327A8',
    'TA8AAA24AQA', 'AAAAAAAAAAAAA', '39A5T824Q7J6K', 'Q286JK395A47T',
    '54TQKJ69327A8', 'Q286JK395A47TQ286JK395A47T',
    'Q286JKKKKK395AAA47TQ286JK395A47T',
    'AAAAAAAAAAAAAQ286JK395A47TQ286JK395A47T'
]


def solution(cards):
    return sorted(cards, key='A23456789TJQK'.index)


@pytest.mark.parametrize('n', TEST_CARDS)
def test_basic_tests(n):
    from sort_cards import sort_cards
    assert sort_cards(n) == solution(n)


def random_tests(SORTED_CARDS):
    from sort_cards import sort_cards
    for _ in range(100):
        random_cards = [choice(SORTED_CARDS) for i in range(randint(1, 100))]
        random_cards = repr(random_cards)
        assert sort_cards(random_cards) == solution(random_cards)
