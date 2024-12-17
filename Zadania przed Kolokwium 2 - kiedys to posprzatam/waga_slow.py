def calc_mass(s1, s2):
    vowels = ["A", "E", "I", "U", "O", "Y"]
    s1_vowel_count = 0
    s1_ascii_sum = 0
    s2_vowel_count = 0
    s2_ascii_sum = 0

    for symbol in s1:
        s1_ascii_sum += ord(symbol)
        if symbol in vowels:
            s1_vowel_count += 1

    for symbol in s2:
        s2_ascii_sum += ord(symbol)
        if symbol in vowels:
            s2_vowel_count += 1

    return s1_vowel_count == s2_vowel_count and s1_ascii_sum == s2_ascii_sum


def wyraz(s1, s2) -> bool:
    def rek(new_s, index):
        nonlocal s1, s2, result
        if calc_mass(s1, new_s):
            result = new_s
            return True

        if index >= len(s2):
            return False

        return rek(new_s + s2[index], index + 1) or rek(new_s, index + 1)

    result = None
    flag = rek("", 0)
    print(f"the result that matches {s1} is {result}")
    return flag


print(wyraz("ula", "sexb"))
