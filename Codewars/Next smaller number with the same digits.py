def next_smaller(n):
    n = str(n)
    for i in range(len(n) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            digit_1 = int(n[i])
            digit_2 = int(n[j])
            if digit_2 > digit_1:
                list_of_digits = list(n)
                list_of_digits[j], list_of_digits[i] = list_of_digits[i], list_of_digits[j]
                if list_of_digits[0] != '0':
                    return int(''.join(list_of_digits))
                return -1
    return -1

