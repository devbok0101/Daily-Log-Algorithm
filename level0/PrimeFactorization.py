#https://school.programmers.co.kr/learn/courses/30/lessons/120852
import math


def solution(n):
    nums = [2,3,5,7, 11, 13, 17, 19]
    answer = []

    for num in nums:
        while n % num == 0:
            if num not in answer:
                answer.append(num)
            n = n // num

    if n != 1:
        answer.append(n)

    return answer




def sol():
    for num in range(2, 10001):
        print(solution(num))

#print(solution(17))
#print(solution(2197))
print(solution(1331))
#print(solution(10000))
print(sol())