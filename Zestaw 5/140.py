def zad140(T,mase):
    def rek(T,mase,i):
        if mase==0:
            return True
        if i>=len(T) or mase<0:
            return False
        return rek(T,mase,i+1) or rek(T,mase-T[i],i+1) 
    return rek(T,mase,0)


T=[1,3,7,8]
print(zad140(T,5))

def zad141(T,mase):
    def rek(T,mase,i):
        if mase==0:
            return True
        if i>=len(T):
            return False
        return rek(T,mase,i+1) or rek(T,mase-T[i],i+1) or rek(T,mase+T[i],i+1)
    return rek(T,mase,0)

print(zad141(T,5))


