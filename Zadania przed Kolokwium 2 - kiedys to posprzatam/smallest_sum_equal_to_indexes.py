'''Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy 
(w sensie liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów 
tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru. 
Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.'''


def solve(T):
    def rek(sum_of_indexes, sum_of_values, amout_of_taken, current_index):
        nonlocal T, result_value, result_size
        if sum_of_indexes == sum_of_values and amout_of_taken != 0 and amout_of_taken < result_size:
            result_size = amout_of_taken
            result_value = sum_of_indexes

        if current_index >= len(T):
            return

        # brać
        rek(sum_of_indexes + current_index, sum_of_values +
            T[current_index], amout_of_taken + 1, current_index + 1)
        # albo nie brać
        rek(sum_of_indexes, sum_of_values, amout_of_taken, current_index + 1)
        # oto jest pytanie

    result_value = None

    result_size = float('inf')

    rek(0, 0, 0, 0)

    return result_value


T = [1, 7, 3, 5, 11, 2]

print(solve(T))
