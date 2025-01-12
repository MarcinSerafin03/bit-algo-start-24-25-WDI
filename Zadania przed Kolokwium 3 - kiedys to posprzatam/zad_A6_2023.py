from math import log10
from linked_lists_util import *


def insert(p, n):
    head = p
    beginning = n//(10**(int(log10(n))))
    ending = n % 10
    first = None
    last = None
    flag = True
    while flag:
        first_digit = head.val//(10**(int(log10(head.val))))
        if first_digit == beginning:
            cnt = 1
            first = head
            head = head.next

            while flag:
                last_digit = head.val % 10
                if last_digit == ending:
                    last = head
                    flag = False
                head = head.next
                cnt += 1

                if head.next == first:
                    return 0

        head = head.next
        if not first and head == p:
            return 0

    head = p
    prev = p
    head = head.next
    while True:
        if head == first:
            prev.next = Node(n, last.next)
            return cnt
        prev = head
        head = head.next


T = [2023, 31, 17, 704, 47, 707, 72, 29, 902]

p = list_to_ll_cycle(T)

print(insert(p, 304))
