"""
Zadanie 201. Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do
funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do
scalonej listy. - funkcja iteracyjna, - funkcja rekurencyjna
"""
from linked_lists_util import *

'''nielegalna wersja (w sensie legalna ale sort jest troche przesadzony tu)'''


def scal_sorted(p, q):
    while p is not None:
        p = p.next
    p.next = q

    return bubble_sort_swap_nodes(p)


def bubble_sort_swap_nodes(head: Node):
    if head is None or head.next is None:
        return head

    swapped = True
    while swapped:
        swapped = False
        prevNode = head
        current = head

        while current.next is not None:

            ptr = current.next
            if current.val > ptr.val:
                swapped = True

                if current == head:  # na początku
                    current.next = ptr.next
                    ptr.next = current
                    prevNode = ptr
                    head = prevNode
                else:  # w środku
                    current.next = ptr.next
                    ptr.next = current
                    prevNode.next = ptr
                    prevNode = ptr
                continue
            prevNode = current
            current = ptr

        display(head)
    return head


def scal_sorted(p: Node, q: Node):
    current_p = p
    prev = None
    while current_p is not None:
        if q is not None and q.val < current_p.val:
            next_q = q.next
            if prev is None:
                q.next = p
                p = q
            else:
                prev.next = q
                q.next = current_p
            prev = q
            q = next_q

        else:
            prev = current_p
            current_p = current_p.next

    if prev is not None:
        prev.next = q
        return p
    else:
        return q


p = list_to_ll([1, 2, 2, 4])
q = list_to_ll([0, 2, 3, 7, 8])

display(scal_sorted(p, q))
