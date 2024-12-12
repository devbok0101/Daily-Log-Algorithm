#https://school.programmers.co.kr/learn/courses/30/lessons/120848
from math import factorial


def solution(n):
    answer = 0
    for i in range (1, 11):
        if factorial(i) >= n:
            answer = i
    return answer


def solution(n):
    answer = 0
    for i in range (1, 12):
        if factorial(i) >= n:
            answer = i - 1
            break
    return answer


print(solution(3628800))