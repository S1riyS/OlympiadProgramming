l = int(input())
r = int(input())
a = int(input())


def solution(l, r, a):
    answer = 0
    for i in range(1, r - l + 1):
        if i % a == 0:
            answer += (r - i - l + 1)
    return answer


print(solution(l, r, a))

# 60 / 100