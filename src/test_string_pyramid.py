"""Tests for the string pyramid module, taken from Code Wars."""

from string_pyramid import watch_pyramid_from_above, watch_pyramid_from_the_side, count_all_characters_of_the_pyramid, count_visible_characters_of_the_pyramid
from random import choice, randint
from string import ascii_letters, digits, punctuation

VALID_CHARS = '{}{}{}'.format(ascii_letters, digits, punctuation)


# ---------Code Wars' correct solutions for testing purposes-------------------

def example_watch_pyramid_from_the_side(characters):
    width = 2 * len(characters) - 1
    output = '{{:^{}}}'.format(width).format
    return '\n'.join(output(char * dex) for char, dex in
                     zip(reversed(characters), range(1, width + 1, 2)))


def example_watch_pyramid_from_above(characters):
    width = 2 * len(characters) - 1
    dex = width - 1
    result = []
    for a in range(width):
        row = []
        for b in range(width):
            minimum, maximum = sorted((a, b))
            row.append(characters[min(abs(dex - maximum), abs(0 - minimum))])
        result.append(''.join(row))
    return '\n'.join(result)


def example_count_visible_characters_of_the_pyramid(characters):
    return (2 * len(characters) - 1) ** 2


def example_count_all_characters_of_the_pyramid(characters):
    return sum(a ** 2 for a in range(1, 2 * len(characters), 2))


def random_string():
    return ''.join(choice(VALID_CHARS) for _ in range(randint(1, 10)))


# ----------------------- None or Empty Tests ---------------------------------


def test_pyramid_handles_none_and_empty_inputs():
    """Test that pyramid handles none and empty inputs."""
    assert watch_pyramid_from_the_side(None) is None
    assert watch_pyramid_from_above(None) is None
    assert count_visible_characters_of_the_pyramid(None) == -1
    assert count_all_characters_of_the_pyramid(None) == -1
    assert watch_pyramid_from_the_side('') == ''
    assert watch_pyramid_from_above('') == ''
    assert count_visible_characters_of_the_pyramid('') == -1
    assert count_all_characters_of_the_pyramid('') == -1


# --------------------------- Basic Tests -------------------------------------


def test_pyramid_can_handle_two_characters():
    """Test that pyramid handles two characters."""
    assert watch_pyramid_from_the_side(
        '*#') == example_watch_pyramid_from_the_side('*#')
    assert watch_pyramid_from_above(
        '*#') == example_watch_pyramid_from_above('*#')
    assert count_visible_characters_of_the_pyramid(
        '*#') == example_count_visible_characters_of_the_pyramid('*#')
    assert count_all_characters_of_the_pyramid(
        '*#') == example_count_all_characters_of_the_pyramid('*#')


def test_pyramid_can_handle_three_characters():
    """Test that pyramid handles three characters."""
    assert watch_pyramid_from_the_side(
        'abc') == example_watch_pyramid_from_the_side('abc')
    assert watch_pyramid_from_above(
        'abc') == example_watch_pyramid_from_above('abc')
    assert count_visible_characters_of_the_pyramid(
        'abc') == example_count_visible_characters_of_the_pyramid('abc')
    assert count_all_characters_of_the_pyramid(
        'abc') == example_count_all_characters_of_the_pyramid('abc')


def test_pyramid_can_handle_same_three_characters():
    """Test that pyramid handles the same 3 characters repeated."""
    assert watch_pyramid_from_the_side(
        'aaa') == example_watch_pyramid_from_the_side('aaa')
    assert watch_pyramid_from_above(
        'aaa') == example_watch_pyramid_from_above('aaa')
    assert count_visible_characters_of_the_pyramid(
        'aaa') == example_count_visible_characters_of_the_pyramid('aaa')
    assert count_all_characters_of_the_pyramid(
        'aaa') == example_count_all_characters_of_the_pyramid('aaa')


def test_pyramid_can_handle_5_descending_ordered_characters():
    """Test that pyramid handles 5 characters in descending order."""
    assert watch_pyramid_from_the_side(
        '54321') == example_watch_pyramid_from_the_side('54321')
    assert watch_pyramid_from_above(
        '54321') == example_watch_pyramid_from_above('54321')
    assert count_visible_characters_of_the_pyramid(
        '54321') == example_count_visible_characters_of_the_pyramid('54321')
    assert count_all_characters_of_the_pyramid(
        '54321') == example_count_all_characters_of_the_pyramid('54321')


# ---------------------------- Random Tests -----------------------------------

def test_pyramid_with_random_inputs():
    """Test that pyramid handles random inputs."""
    for _ in range(100):
        characters = random_string()
        assert watch_pyramid_from_the_side(
            characters) == example_watch_pyramid_from_the_side(characters)
        assert watch_pyramid_from_above(
            characters) == example_watch_pyramid_from_above(characters)
        assert count_visible_characters_of_the_pyramid(
            characters) == example_count_visible_characters_of_the_pyramid(
            characters)
        assert count_all_characters_of_the_pyramid(
            characters) == example_count_all_characters_of_the_pyramid(
            characters)
