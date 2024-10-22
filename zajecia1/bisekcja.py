def bisection(): #x^x - 2020 = 0
    a = 1
    b = 200
    while b - a >= 1e-10:
        x = (a + b)/2
        if x**x >= 2020:
            b = x
        else:
            a = x
    return (a + b)/2

x = bisection()

print(f"x = {x}, x^x = {x**x}") #fstring - warto poczytać!

#https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/