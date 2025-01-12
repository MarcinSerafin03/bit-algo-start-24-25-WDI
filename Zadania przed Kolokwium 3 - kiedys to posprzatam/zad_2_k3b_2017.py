from linked_lists_util import *


def split_y_list(A, B):
    if A.next is None or B.next is None:
        return
    result = 0
    current_a = A
    while current_a.next is not None:
        current_b = B
        while current_b.next is not None:
            if current_b.next.val == current_a.next.val:
                support = current_a.next
                while support is not None:
                    current_a.next = Node(support.val)
                    current_a = current_a.next
                    support = support.next
                    result += 1
                return result

            current_b = current_b.next
        current_a = current_a.next
    return result


A = list_to_ll([5, 11])
B = list_to_ll([13, 7, 17])
C = list_to_ll([3, 2])

A.next.next = C
B.next.next.next = C

display(A)
display(B)

print(split_y_list(A, B))
display(A)
display(B)
