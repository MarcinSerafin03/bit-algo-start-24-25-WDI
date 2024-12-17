def rook(N,L):
    def rek(N,L,y,x,cnt):
        mini = float('inf')
        if y==x==7:
            return cnt
        for i in range(y+1,N):
            if (i,x) in L:
                break
            mini=min(mini,rek(N,L,i,x,cnt+1))
 
        for i in range(x+1,N):
            if (y,i) in L:
                break
            mini=min(mini,rek(N,L,y,i,cnt+1))
        
        return mini
    res = rek(N,L,0,0,0)
    return res if res!=float('inf') else None

L = [(7,6),(6,7)]
print(rook(8,L))


        
