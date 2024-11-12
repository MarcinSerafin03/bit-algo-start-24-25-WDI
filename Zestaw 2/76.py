def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def mask_sume(t1, t2, mask):
    sume = 0
    T=[0]*len(t1)
    for i in range(len(t1)):
        if mask % 3 == 0:
            sume += t1[i]
            T[i] = t1[i]
        elif mask % 3 == 1:
            sume += t2[i]
            T[i] = t2[i]
        elif mask % 3 == 2:
            sume += t1[i] + t2[i]
            T[i] = t1[i] + t2[i]
        mask //= 3

    return sume,T


def ex76(t1, t2):
    cnt = 0
    for mask in range(3 ** len(t1)):
        sume,T=mask_sume(t1, t2, mask)
        if is_prime(sume):
            print("Sume ",sume," Array: ",T)
            cnt += 1

    return cnt


t1 = [1, 3,2,4]
t2 = [9,7,4,8]

#1+3=4
#1+4=5 +
#2+3=5 +
#2+4=6
#1+3+4=8
#1+2+4=7 +
#3+1+2=6
#3+2+4=9
#1+3+2+4=10

print(ex76(t1, t2))
