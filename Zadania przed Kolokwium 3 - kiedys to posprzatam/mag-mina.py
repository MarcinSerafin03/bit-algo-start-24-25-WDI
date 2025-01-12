'''
(zwykłe domino stworzone przez maga xd)

3. Dane są deklarację reprezentujące listę z klockami mag-mina (patrz zadanie 2). 
struct klocek { int a; int b; klocek *next; }; Lista zawiera zestaw klocków, które można ułożyć w ciąg. 
Niestety klocki pomieszały się. Proszę napisać funkcję, która ustawia klocki na liście w ciąg. 
Uwaga: orientacja klocków w liście jest właściwa. Na przykład listę: 
[2|9] [3|6] [8|2] [2|3] [6|2] należy przekształcić na listę: [8|2] [2|3] [3|6] [6|2] [2|9]
'''


class Klocek:
    def __init__(self, a, b, next=None):
        self.a = a
        self.b = b
        self.next = next


def list_to_ll(List: list):
    """Convert list to linked list"""
    head = current = Klocek(List[0][0], List[0][1])
    for i in range(1, len(List)):
        new = Klocek(List[i][0], List[i][1])
        current.next = new
        current = new
    return head


def display(head):
    """Display the linked list"""
    current = head
    while current:
        print(f"[{current.a} | {current.b}]", end=" ")
        current = current.next
    print()


def get_size(p):
    result = 0
    while p is not None:
        result += 1
        p = p.next
    return result


def mag_mina(p):
    n = get_size(p)
    Klocek_list = [None for _ in range(n)]
    iterator = 0
    while p is not None:
        Klocek_list[iterator] = p
        p = p.next
        Klocek_list[iterator].next = None
        iterator += 1

    def mag_mina_rekur(curent_setup, curent_setup_i, Klocek_rest):
        nonlocal result, Klocek_list
        if curent_setup_i == len(curent_setup):
            result = [Klocek(klocek.a, klocek.b) for klocek in curent_setup]
            return

        for i in range(len(Klocek_rest)):
            if Klocek_rest[i]:
                klocek = Klocek_list[i]
                if curent_setup[curent_setup_i-1] is None or curent_setup[curent_setup_i-1].b == klocek.a:
                    curent_setup[curent_setup_i] = klocek
                    Klocek_rest[i] = False
                    mag_mina_rekur(
                        curent_setup, curent_setup_i + 1, Klocek_rest)
                    curent_setup[curent_setup_i] = None
                    Klocek_rest[i] = True

    result = None

    mag_mina_rekur([None for _ in range(n)], 0, [True for _ in range(n)])

    for i in range(1, n):
        result[i-1].next = result[i]

    return result[0]


p = list_to_ll([(2, 9), (3, 6), (8, 2), (2, 3), (6, 2)])
new_p = mag_mina(p)
display(new_p)
