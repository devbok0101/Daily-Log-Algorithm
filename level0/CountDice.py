#https://school.programmers.co.kr/learn/courses/30/lessons/120845

from math import prod

def solution(box, n):
    answer = 1

    for length in box:
        answer *= (length // n)

    return answer

# prod == *= 와 동일하다.
def solution2(box, n):
    return prod([length // n for length in box])

print(solution([10,8,6], 3))
print(solution([1,1,1], 1))