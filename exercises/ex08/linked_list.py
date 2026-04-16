"""A few algorithms to process a singly-linked list data"""

from __future__ import annotations

__author__ = "730558495"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the value at a given index in a linked list"""
    if head is None:  # edge case for empty list
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # base case for index 0
        return head.value
    else:  # recursive case
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns the maximum value in a linked list."""
    if head is None:  # edge case for an empty list
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value

    # Create an integer place holder for Node | None variable head.next. Follows rest = function(parameter) format
    rest: int = max(head.next)
    if head.value > rest:
        return head.value
    else:
        return rest


def linkify(items: list[int]) -> Node | None:
    """Converts a list of ints to a linked list."""
    if len(items) == 0:  # can serve as both edge and base case
        return None

    idx: int = 0
    rest: Node | None = linkify(items[idx + 1 : len(items)])
    new_linked_list: Node | None = Node(items[idx], rest)
    # items[idx] because linked list requires Node(value, rest) format
    return new_linked_list


def scale(head: Node | None, factor: int) -> Node | None:
    """Scales a linked list by a given factor."""
    if head is None:
        return None

    rest: Node | None = scale(head.next, factor)
    new_linked_list: Node | None = Node(head.value * factor, rest)
    return new_linked_list
