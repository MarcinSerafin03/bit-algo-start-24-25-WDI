def is_repetitive(word):
    l = len(word)
    for i in range(1, l // 2 + 1):  # i - length of smaller word/pattern
        if l % i == 0:
            pattern = word[:i] # word = ABCABCABC word[0:3] == ABC
            print(pattern,i)
            # abc * 3 = abcabcabc
            if pattern * (l // i) == word:
                return True
    return False


def multi(T):
    maxi = 0
    for word in T:
        if is_repetitive(word):
            maxi = max(maxi, len(word))
    return maxi

# for word in T == for i in range(len(T)): word=T[i]

print(multi(['ABCABCABC', 'AAAA', 'sdfchijnusdfjio']))
