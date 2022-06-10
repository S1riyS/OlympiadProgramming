from math import sqrt


def decomp(number):
    def add_to_powers(n):
        if n in powers:
            powers[n] += 1
        else:
            powers[n] = 1

    powers = {}

    for i in range(2, number + 1):
        local_number = i
        for j in range(2, int(sqrt(local_number)) + 1):
            while local_number % j == 0:
                add_to_powers(j)
                local_number //= j

        if local_number != 1:
            add_to_powers(local_number)

    result = []
    for prime, power in powers.items():
        if power != 1:
            result.append(f'{prime}^{power}')
        else:
            result.append(str(prime))

    return ' * '.join(result)

print(decomp(3990))
