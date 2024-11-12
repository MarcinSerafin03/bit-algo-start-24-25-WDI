def decimal_to_base_k(number, K):
    if number == 0:
        return '0'

    numbers = ['0', '1', '2', '3', '4', '5', '6',
               '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    result = ''

    while number > 0:
        remainder = number % K
        result += numbers[remainder]
        number //= K

    return result
