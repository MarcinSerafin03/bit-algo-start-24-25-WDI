def zad2(T):
    N = len(T)
    res = -1
    def rek(T,i,cnt):
        nonlocal res
        if i==N-1:
            #return cnt
            res = cnt
        if i>=N:
            # return float('inf')
            return
        num = T[i]
        k=2
        #mini = float('inf')
        while num>1:
            if num%k:
                k+=1
            else:
                #mini = min(mini,rek(T,i+k,cnt+1))
                rek(T,i+k,cnt+1)
                num/=k
        #return mini
    

    #res = rek(T,0,0)
    rek(T,0,0)
    return res #if res<float('inf') else -1

T=[4,3,5,0,0,0,0,0]

print(zad2(T))