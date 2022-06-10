def beeramid(bonus, price):
    if bonus < 0:
        cans = 0
    else:
        cans = bonus // price

    levels = 0
    cans_used = 0
    while cans_used <= cans:
        levels += 1
        cans_used += levels ** 2

    return levels - 1

print(beeramid(14, 1))