def przeliczanko(n, base):
    res = 0
    i = 0
    while n > 0:
        res += (n % base) * 10 ** i
        i += 1
        n //= base
    return res


print(przeliczanko(23, 4))
