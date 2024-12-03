# https://school.programmers.co.kr/learn/courses/30/lessons/120840
import math


def solution(balls, share):
    balls_share = balls - share
    return math.factorial(balls) // (math.factorial(share)) * (math.factorial(balls_share))

#print(solution(3, 2))
print(solution(5, 3))
