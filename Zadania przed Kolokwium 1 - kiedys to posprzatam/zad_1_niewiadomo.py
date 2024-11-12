def decimal_to_base4(number):
    base4 = 0
    multiplier = 1

    while number > 0:
        remainder = number % 4
        base4 += remainder * multiplier
        number //= 4
        multiplier *= 10

    return base4


print(decimal_to_base4(10))  # Output: 22
print(decimal_to_base4(7))   # Output: 13
print(decimal_to_base4(0))   # Output: 0


def check_4_correct(N4_1, N4_2):
    N4_1_numbers = [False for _ in range(4)]
    N4_2_numbers = [False for _ in range(4)]

    while N4_1 > 0:
        N4_1_numbers[N4_1 % 10] = True
        N4_1 //= 10

    while N4_2 > 0:
        N4_2_numbers[N4_2 % 10] = True
        N4_2 //= 10

    for i in range(4):
        if N4_1_numbers[i] != N4_2_numbers[i]:
            return False

    return True


def zad2(T):
    n = len(T)
    longest = 1
    for i in range(n):
        longest_pretender = 1
        for j in range(i+1, n):
            if check_4_correct(decimal_to_base4(T[i]), decimal_to_base4(T[j])):
                longest_pretender += 1
        longest = max(longest, longest_pretender)

    return longest
