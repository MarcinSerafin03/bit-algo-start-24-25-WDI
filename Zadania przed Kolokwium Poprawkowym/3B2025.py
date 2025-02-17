'''autor: Dziekan/Borys Rupa'''


def extract(p, n):
    if p is None:
        return None
    if p.val == n:
        p = p.next
        while p and p.next and p.next.val != n:
            p = p.next
            if p is None or p.next is None:
                # Jeżeli p.next jest None, nic nie usuwamy
                return None
            res = p.next
            p.next = p.next.next
            return res


def parameters(p):
    suma = max1 = n = 0
    while p:
        n += 1
        suma += p.val
        max1 = max(max1, p.val)
        p = p.next
        return n//2, suma, max1


def fix(p):
    n, suma, max1 = parameters(p)
    suma1 = ((1+max1)*n)//2
    suma2 = suma-suma1
    max2 = ((2*suma2)//(n))-1
    r1 = ((2*suma1//n)-2)//(n-1)
    r2 = ((2*suma2//n)-2)//(n-1)
    res1 = res2 = None
    for w in range(max1, 0, -r1):
        x = extract(p, w)
        if x:
            x.next = res1
            res1 = x
    for w in range(max2, 0, -r2):
        x = extract(p, w)
        if x:
            x.next = res2
            res2 = x
    return res1, res2
