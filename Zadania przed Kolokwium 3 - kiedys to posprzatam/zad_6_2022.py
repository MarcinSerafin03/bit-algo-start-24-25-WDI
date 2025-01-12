'''
Zadanie 6 (5 pkt)
Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

Lista zawierała wartości stanowiące kolejne wyrazy ciągu geometrycznego. Z wnętrza listy usunięto
pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy),
która uzupełnia listę elementami, tak aby ponownie zawierała kolejne wyrazy ciągu geometrycznego.
Funkcja powinna zwrócić liczbę wstawionych elementów. Na przykład poniższa lista zostanie przekształcona:
4 -32 -128 -2048 −→ 4 -8 16 -32 64 -128 256 -512 1024 -2048 (zostanie zwrócona wartość 6)
Można założyć, że lista wejściowa liczy więcej niż 2 elementy i każdy element listy jest liczbą całkowitą rózną od 0 (iloraz ciągu nie musi być całkowity).
'''

from linked_lists_util import *
import time


def insert(prev: Node, node_to_insert: Node, next: Node):
    prev.next = node_to_insert
    node_to_insert.next = next


def repair(p):
    head = p
    p_test = head
    while p_test is not None:
        prev = p_test
        current = p_test.next
        flag = True
        print(f"current {current.val}")
        while current is not None:
            if current.next is not None:
                q = current.next.val / current.val
                print(f"q = {q}")
                if p_test.val * q != current.val:
                    time.sleep(1)
                    flag = False
                    new = Node(p_test.val * q)
                    if abs(q) > 1:
                        if abs(p_test.val * q) > abs(current.val):
                            insert(current, new, current.next)
                        else:
                            insert(prev, new, current)
                    else:
                        if abs(p_test.val * q) > abs(current.val):
                            print(f"Inserting {new.val} here")
                            insert(prev, new, current)
                        else:
                            print(f"Inserting {new.val} here 2")
                            insert(current, new, current.next)
                break

            else:
                current = current.next
        display(head)
        if flag:
            p_test = p_test.next

    return head


p = list_to_ll([4, -32, -128, -2048])

display(repair(reverse_linked_list(p)))
