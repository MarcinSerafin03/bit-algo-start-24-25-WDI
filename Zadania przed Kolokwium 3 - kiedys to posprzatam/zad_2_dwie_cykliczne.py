"""
2. Dane są dwie listy cykliczne powstałe przez zapętlenie listy [list] jednokierunkowej posortowanej
rosnąco, dla każdej listy dany jest wskaźnik wskazujący przypadkowy element w takiej liście.
Proszę napisać funkcję, która dla dwóch list cyklicznych, usuwa z obu list elementy
występujące w obu listach. Do funkcji należy przekazać wskaźniki na dwie listy, funkcja
powinna zwrócić łączną liczbę usuniętych elementów.
Uwagi:
- czas na rozwiązanie obu zadań wynosi 45 minut
- za każde zadanie można otrzymać maksymalnie 5 pkt
- oceniane będą: czytelność, poprawność i efektywność rozwiązań
"""
from linked_lists_util import *


def remove_same(p: Node, q: Node):
    while p.val < p.next.val:
        p = p.next
    p = p.next
    p_begining = p

    while q.val < q.next.val:
        q = q.next
    q = q.next
    q_begining = q

    result = 0
    while q.next != q_begining or p.next != p_begining:

        if p.val == q.val:
            result += 1
            p = p.next
            q = q.next

        elif p.val < q.val:
            p = p.next
        else:
            q = q.next

    if p.val == q.val:
        result += 1

    return result


p = list_to_ll_cycle([1, 2, 3, 5, 7, 8])

q = list_to_ll_cycle([4, 7, 2, 3])

print(remove_same(p, q))
