def zad156(T,R):
    N = len(T)
    def rek(T,R,i,cnt,resistance):
        if cnt > 3:
            return False
        if resistance==R:
            return cnt==3
        if i>=N:
            return False
        return rek(T,R,i+1,cnt+1,resistance+T[i]) or rek(T,R,i+1,cnt,resistance) or rek(T,R,i+1,cnt+1,1/((1/resistance)+(1/T[i])))
    
    return rek(T,R,0,0,0)


T=[1,2,5,8]
R=15
print(zad156(T,R))