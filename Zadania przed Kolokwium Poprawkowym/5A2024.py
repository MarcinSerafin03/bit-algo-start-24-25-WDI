def eight(n):
    tab = [0,0,0,0,0,0,0,0]
    while n > 0:
        div = n % 8
        tab[div] += 1
        if tab[div] > 1:
            return False
        n = n // 8
    return True

def is_proper(T,i,j,k):
    for row in range(i,i+k):
        for col in range(j,j+k):
            if not eight(T[row][col]):
                return False
    return True

def square(T):
    maxi = 0
    for i in range(len(T)):
        for j in range(len(T)):
            for k in range(len(T)-max(i,j)):
                if is_proper(T,i,j,k):
                    maxi = max(maxi,k)
        if i>len(T)-maxi:
            return maxi
    return maxi
                
t=[[1, 2, 218, 466, 371, 496,  76, 300, 499, 190], 
   [ 3, 4, 184, 175, 496, 288, 462, 367,  75,  21], 
   [455,  43, 306, 220,  24, 202,  83, 337,  24,  80], 
   [134, 263, 106, 307,   1, 313, 285, 496, 390, 452], 
   [470, 237, 382, 419, 426, 179, 366,   5, 119, 452], 
   [154, 314,  74, 321, 445, 306, 359, 415, 155, 175], 
   [  2, 184, 441, 108, 250,  68,   1, 372,  96, 255], 
   [104, 339, 175, 300,  62, 193, 456, 439, 225, 400], 
   [159,  46, 382, 216,   7, 362, 349, 325,  96,  60], 
   [161,  39, 146,  57, 310, 101, 274, 172,  22, 440]]

print(square(t))

        