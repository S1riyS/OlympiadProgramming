"""
6 kyu

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""

def count_bits(n):
    bits = []
    while n != 0:
        bit = n % 2
        bits.append(bit)
        n = n // 2

    return bits.count(1)

