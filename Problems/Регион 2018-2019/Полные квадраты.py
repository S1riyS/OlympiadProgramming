from math import sqrt

k = int(input())

def is_square(n):
    return sqrt(n).is_integer()

def solution(number):
    if number < 0:
        if is_square(abs(number)):
            return 0

    for i in range(1, round(sqrt(number)) + 1):
        if number % i == 0:
            b1 = i
            b2 = number // i
            a = abs((b1 + b2) // 2)
            n = abs((b1 - b2) // 2)
            print(b1, b2, a, n)
            return a

print(solution(k))
