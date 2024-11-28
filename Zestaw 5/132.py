def zad132(n,k):
    def rek(n,k):
        if n==0 or n==k or k==0:
            return 1   
        return rek(n-1,k-1)+rek(n-1,k)
    return rek(n,k)

print(zad132(7,2))
