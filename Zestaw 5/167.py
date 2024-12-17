def zad167(word):
    T=['a','e','i','y','o','u']
    def rek(i,flag,word):
        if word[i] in T:
            if flag:
                return 0
            else:
                flag=True
        if i==len(word)-1:
            if flag:
                return 1
            else:
                return 0
        if flag:
            return rek(i+1,flag,word) + rek(i+1,False,word)
        else:
            return rek(i+1,flag,word)
    return rek(0,False,word)

print(zad167("alicja"))
