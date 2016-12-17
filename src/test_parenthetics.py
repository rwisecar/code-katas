"""Test parenthetics.py."""

from parenthetics import Node, DoubleLink
import pytest


@pytest.fixture
def full_list():
    new_list = DoubleLink(iterable=[1, 2, 3])
    return new_list


def test_create_node():
    """Test whether we create a node with a value 'val'."""
    test_node = Node(15)
    assert test_node.value == 15


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
    new_list = DoubleLink(1)
    assert new_list._length == 1


def test_create_multi_value_list(full_list):
    """Test that you can create list with iterable."""
    assert full_list._length == 3


def test_push_new_node_to_full_dll(full_list):
    """Test that you can push a new value to a nonempty list."""
    full_list.push(15)
    assert full_list.head.value == 15


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


