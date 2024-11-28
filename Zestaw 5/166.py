from math import factorial


def find_reconstruction(T1, T2):
    def recontruct(T, T_check, accumulator):
        nonlocal T_result, cur_index
        n = len(T)

        # warunek końcowy
        flag = False
        for i in range(n):
            if T_check[i]:
                flag = True

        if not flag:
            T_result[cur_index] = accumulator
            cur_index += 1
            return

        # krok rekurencji
        for i in range(n):
            if T_check[i]:
                T_check[i] = False
                recontruct(T, T_check, accumulator + T[i])
                T_check[i] = True

    T_result = ["" for _ in range(factorial(len(T1)))]
    cur_index = 0

    recontruct(T1, [True for _ in range(len(T1))], "")

    T1_result = T_result

    T_result = ["" for _ in range(factorial(len(T2)))]
    cur_index = 0

    recontruct(T2, [True for _ in range(len(T2))], "")

    T2_result = T_result

    potential_result = ""

    for t1 in T1_result:
        for t2 in T2_result:
            if t1 == t2:
                if potential_result == "":
                    potential_result = t1
                # check if its different matching
                elif potential_result != t1 and potential_result != t2:
                    return "brak możliwości jednoznacznego odtworzenia napisu"

    return potential_result if potential_result != "" else "brak możliwości jednoznacznego odtworzenia napisu"


# correct case ("ab" and "cde" are merged)
T1 = ["abcde", "cfed", "fab"]
T2 = ["abc", "abc", "def", "fed"]

print(find_reconstruction(T1, T2))

# incorrect case
T1_bad = ["ab", "ba"]
T2_bad = ["ab", "ba"]

print(find_reconstruction(T1_bad, T2_bad))
