def A(x):
    if len(str(x)) >= 2:
        return int(str(x)[:-2] + str(x)[-1] + str(x)[-2])
    return x


def B(x):
    return x * 3


def C(x):
    if len(str(x)) >= 2:
        return int(str(x)[1:])
    return x

# raczej na pewno nie trzeba implementowac A, B i C ale warto się zapytać na kolokwium


def check(x, y):
    def rek(potential_result_string, x, y, num_of_operations):
        nonlocal result
        if num_of_operations > 7:
            return
        if x == y:
            if result == "" or len(result) > len(potential_result_string):
                result = potential_result_string
            return

        rek(potential_result_string + "A", A(x), y, num_of_operations + 1)
        rek(potential_result_string + "B", B(x), y, num_of_operations + 1)
        rek(potential_result_string + "C", C(x), y, num_of_operations + 1)

    result = ""
    rek("", x, y, 0)
    return result


print(check(6, 3))
