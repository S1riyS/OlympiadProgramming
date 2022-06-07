# https://codeforces.com/gym/102906/problem/A
# 100 / 100

n = int(input())
m = int(input())

def solution(boys, girls):
    return min(boys, girls) * 2 + (max(boys, girls) - min(boys, girls)) % 2

print(solution(n, m))