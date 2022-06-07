"""
1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1
"""
arr = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1]


def get_power_of_2(number: int) -> int:
    power = 1
    while 2 ** power < number:
        power += 1
    return power - 1

