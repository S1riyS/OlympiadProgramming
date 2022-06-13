import sys
import threading


def GCD(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return GCD(a % b, b)
    else:
        return GCD(a, b % a)


def solution():
    n, m = list(map(int, input('N, M - ').split()))
    print(GCD(n, m))


sys.setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=solution)
thread.start()

