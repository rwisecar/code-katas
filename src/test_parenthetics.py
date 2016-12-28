"""Test parenthetics.py."""

from parenthetics import Node, DoubleLink
import pytest


@pytest.fixture
def full_list():
    new_list = DoubleLink([1, 2, 3])
    return new_list


@pytest.fixture
def broken_list():
    new_list = DoubleLink(')())(')
    return new_list


@pytest.fixture
def open_list():
    new_list = DoubleLink(')(()(')
    return new_list


@pytest.fixture
def balanced_list():
    new_list = DoubleLink(')()()()(')
    return new_list


def test_create_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node(')')
    assert test_node.value == ')'


def test_create_empty_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node()
    assert test_node.value is None


def test_create_list_raise_error():
    """Test that TypeError is raised when you init with noniterable."""
    with pytest.raises(TypeError):
        new_dll = DoubleLink(iterable=123456)


def test_test_next_node():
    """Test whether creating a next with another node."""
    test_node1 = Node(15)
    test_node2 = Node(10, next_node=test_node1)
    assert test_node2.next_node.value == 15


def test_test_previous_node():
    """Test whether creating a previous with another previous node."""
    test_node2 = Node(10)
    test_node1 = Node(20, previous_node=test_node2)
    assert test_node1.previous_node.value == 10


def test_create_empty_dll():
    """Test whether we create an empty list."""
    new_list = DoubleLink()
    assert new_list._length is 0


def test_create_one_value_list():
    """Test that you can create list with one value."""
    new_list = DoubleLink(')')
    assert new_list._length == 1


def test_create_multi_value_list(full_list):
    """Test that you can create list with iterable."""
    assert full_list._length == 3


def test_multi_value_list_with_parens():
    """Test that you can create a list with a string of parens."""
    new_list = DoubleLink(')()()()')
    assert new_list.head.value == ')'


def test_push_new_node_to_full_dll(full_list):
    """Test that you can push a new value to a nonempty list."""
    full_list.push(')')
    assert full_list.head.value == ')'


def test_push_next_node(full_list):
    """Test that when you push to a nonempty list, the next node is previous head."""
    full_list.push(15)
    assert full_list.head.next_node.value == 3


def test_push_previous_node(full_list):
    """Test that when you push to a nonempty list, the next node's previous node is the head."""
    full_list.push(15)
    assert full_list.head.next_node.previous_node.value == 15


def test_push_tail_node_empty_list():
    """Test that when you push to an empty list, the head is also the tail."""
    new_list = DoubleLink()
    new_list.push(15)
    assert new_list.tail.value == 15


def test_push_tail_node_full_list(full_list):
    """Test that the tail node is the last node when you make a list."""
    assert full_list.tail.value == 1


def test_balanced_first_node_closed_paren():
    """Check that balanced returns -1 when head is ')'."""
    new_list = DoubleLink('()')
    assert new_list.balanced() == -1


def test_balanced_open_paren(open_list):
    """Test that balanced returns 1 when unmatched open paren."""
    assert open_list.balanced() == 1


def test_balanced_list(balanced_list):
    """Test that balanced list returns 0."""
    assert balanced_list.balanced() == 0


def test_balanced_broken_list(broken_list):
    """Test that broken list returns -1."""
    assert broken_list.balanced() == -1


def test_balanced_no_parens_in_list(full_list):
    """Test that a list with no parens returns a value error."""
    with pytest.raises(ValueError):
        full_list.balanced()


def test_balanced_empty_list():
    """Test that an empty list returns a value error."""
    new_list = DoubleLink()
    with pytest.raises(ValueError):
        new_list.balanced()


def test_balanced_tail_open():
    """Test that a list with an open tail returns 1."""
    new_list = DoubleLink('(()(')
    assert new_list.tail.value == '('
    assert new_list.balanced() == 1


def test_balanced_tail_closed_returns_0():
    """Test that a list with a closed tail returns 0."""
    new_list = DoubleLink(')()(')
    assert new_list.tail.value == ')'
    assert new_list.balanced() == 0

