"""
Азату стало интересно, сколько существует пар целочисленных корней (x1,x2), которые являются корнями уравнения x2+bx+c=0,
где сумма коэффициентов b и c лежит между l и r, то есть l≤b+c≤r (b, c, l, r — целые числа).
Пары корней (x1,x2) и (x2,x1) считаются одинаковыми.

Помогите Азату узнать ответ на его задачку
"""
from math import sqrt


def get_divisors(number: int) -> list:
    divisors = []

    for i in range(1, round(sqrt(number)) + 1):
        if number % i == 0:
            divisors.append(i)
            divisors.append(number // i)

    return list(set(divisors))

l, r = list(map(int, input().split()))

# Если l = r:
# Преобразовывая т. Виета, получаем (x1 - 1)(x2 - 1) = l + 1
# Т.е (x1 - 1) и (x2 - 1) - делители числа (l + 1)

divisors = get_divisors(l + 1)
print(len(divisors) + 1)
