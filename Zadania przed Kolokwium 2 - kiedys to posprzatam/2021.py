def square(T):
    def only_two_primes(num):
        a=0
        b=0
        i=2
        while num>1:
            if num%i:
                i+=1
            else:
                if a and b and i!=a and i!=b:
                    return False
                if a and not b and i!=a:
                    b=i
                if not a:
                    a=i
                num/=i
        return True


    N = len(T)
    mini = float('inf')
    for y in range(0,N-1):
        for x in range(0,N-1):
            for i in range(max(x,y)+1,N):
                if only_two_primes(T[y][x]*T[y+i][x]*T[y][x+i]*T[y+i][x+i]):
                    mini=min(mini,i-max(x,y)+1)
    return mini if mini!=float('inf') else 0


