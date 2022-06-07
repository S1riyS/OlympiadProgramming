# https://codeforces.com/gym/102906/problem/B
# 100 / 100

a = int(input())
b = int(input())
k = int(input())

def get_row(row_number, delete):
    start = row_number * (row_number - 1) // 2 + 1
    if row_number < delete:
        return [i for i in range(start, start + row_number)]
    return [i for i in range(start, start + delete)]

def solution(low, high, delete):
    for i in range(low, high + 1):
        print(*get_row(i, delete))

solution(a, b, k)