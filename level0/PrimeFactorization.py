#https://school.programmers.co.kr/learn/courses/30/lessons/120852
import math


def solution(n):
    answer = []
    d = 2

    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            while n % d == 0:  # 동일 소인수를 모두 제거
                n //= d
        else:
            d += 1

    if n > 1:  # 나머지가 1보다 크다면 소수
        answer.append(n)

    return answer


def sol():
    for num in range(2, 10001):
        print(solution(num))

print(solution(143))
#print(solution(2197))
#print(solution(1331))
#print(solution(10000))
#print(sol())