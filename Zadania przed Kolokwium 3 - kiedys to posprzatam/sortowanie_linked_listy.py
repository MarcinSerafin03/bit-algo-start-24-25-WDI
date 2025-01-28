from linked_lists_util import *


def bubble_sort_swap_val(head: Node):
    if head is None or head.next is None:
        return head

    swapped = True
    while swapped:
        swapped = False
        current = head
        while current is not None and current.next is not None:
            if current.val > current.next.val:
                current.val, current.next.val = current.next.val, current.val
                swapped = True
            current = current.next
        display(head)

    return head


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


head = list_to_ll([4, 2, 5, 1, 3])
print("start")
display(head)

print("process")
head = bubble_sort_swap_nodes(head)

print("result")
display(head)
