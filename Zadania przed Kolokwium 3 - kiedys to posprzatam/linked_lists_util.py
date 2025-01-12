"""Collection of usefull tools for linked lists

Usage:
at the top of the file just type
from linked_lists_util import * (or Node class and any function you want)

or just coppy at the top on your file xdddd
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def display(head):
    """Display the linked list"""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def display_n(head, n):
    """Display the linked list"""
    current = head
    if not current:
        return
    print(current.val, end="")
    current = current.next
    for _ in range(1, n):
        if not current:
            break
        print(" -> " + str(current.val), end="")
        current = current.next
    print()


def list_to_ll(List: list):
    """Convert list to linked list"""
    head = current = Node(List[0])
    for i in range(1, len(List)):
        new = Node(List[i])
        current.next = new
        current = new
    return head


def list_to_ll_cycle(List: list):
    """Convert list to linked list with cycle"""
    head = current = Node(List[0])
    for i in range(1, len(List)):
        new = Node(List[i])
        current.next = new
        current = new
    current.next = head
    return head


def compare_list_to_ll(List: list, head):
    """Compare list between linked list"""
    for i in range(len(List)):
        if head is None:
            return False
        if head.val != List[i]:
            return False
        head = head.next
    return head is None


def reverse_linked_list(head):
    """reverse linked list (duh)"""
    curr = head
    prev = None

    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev


if __name__ == '__main__':
    display(list_to_ll([1, 2, 3, 69, 4, 5, 6]))

    # True
    assert compare_list_to_ll(
        [1, 2, 3, 4], reverse_linked_list(list_to_ll([4, 3, 2, 1])))

    # False
    assert not compare_list_to_ll(
        [1, 2, 3, 4], reverse_linked_list(list_to_ll([3, 4, 2, 1])))

    # True
    assert compare_list_to_ll([1, 2, 3, 69, 4, 5, 6],
                              list_to_ll([1, 2, 3, 69, 4, 5, 6]))

    # False (ll longer)
    assert not compare_list_to_ll(
        [1, 2, 3, 69, 4, 5, 6], list_to_ll([1, 2, 3, 69, 4, 5, 6, 7]))

    # False (list longer)
    assert not compare_list_to_ll(
        [1, 2, 3, 69, 4, 5, 6], list_to_ll([1, 2, 3, 69, 4, 5, 6, 7]))

    # False (diff values)
    assert not compare_list_to_ll([1, 2, 6], list_to_ll([1, 2, 3]))
