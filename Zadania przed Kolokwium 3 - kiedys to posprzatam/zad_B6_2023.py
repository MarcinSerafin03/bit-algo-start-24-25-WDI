"""
Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola key i next, której węzły przechowują liczby całkowite. 
Proszę napisać funkcję separate(p) która rozdziela listę cykliczną na dwie listy cykliczne. Pierwsza powinna zawierać klucze parzyste dodatnie, 
druga klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać wskaźnik na listę z danymi. 

Funkcja powinna zwrócić wskaźniki na powstałe listy oraz liczbę usuniętych elementów.

Uwagi:
• Oceniane będą: czytelność, poprawność i efektywność rozwiązań.
• Czas na rozwiązanie obu zadań 50 minut.
"""
from linked_lists_util import *


def separate(p):
    tmp = p.next
    p.next = None
    p = tmp

    head_even = last_even = None
    head_odd = last_odd = None

    removed = 0

    while p is not None:
        p_next = p.next
        p.next = None
        if p.val < 0 and p.val % 2 == 1:
            if head_odd is None:
                head_odd = last_odd = p
            else:
                last_odd.next = p
                last_odd = last_odd.next
        elif p.val > 0 and p.val % 2 == 0:
            if head_even is None:
                head_even = last_even = p
            else:
                last_even.next = p
                last_even = last_even.next
        else:
            removed += 1

        p = p_next

    if last_even is not None:
        last_even.next = head_even

    if last_odd is not None:
        last_odd.next = head_odd

    return head_even, head_odd, removed


p = list_to_ll_cycle([3, -1, -2, 7, -4, -3, 8, 2])

even, odd, removed = separate(p)


display_n(even, 3)
display_n(odd, 3)
print(removed)
