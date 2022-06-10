def multiply_digits(number):
    digits = list(map(int, list(str(number))))
    result = 1
    for digit in digits:
        result *= digit
    return result


def persistence(n):
    counter = 0
    while n > 9:
        n = multiply_digits(n)
        counter += 1
    return counter


print(persistence(39))
