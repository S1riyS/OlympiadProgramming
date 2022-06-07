# https://codeforces.com/gym/102906/problem/D
# 35 / 100 (Time Limit)

from math import sqrt

def is_square(n):
    return sqrt(n).is_integer()


def get_divisors(number: int):
    divisors = []
    for i in range(1, round(sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number // i)

    return list(set(divisors))

def check_square(n1, n2):
    for z1 in get_divisors(n1):
        for z2 in get_divisors(n2):
            if is_square((n1 * n2) // (z1 * z2)) and (n1 * n2) // (z1 * z2) != 1:
                return True
    return False

L_input = int(input())
R_input = int(input())

def solution(L, R):
    answer = 0
    for a in range(L, R):
        for b in range(a + 1, R + 1):
            if not check_square(a, b):
                answer += 1

    return answer

print(solution(L_input, R_input))