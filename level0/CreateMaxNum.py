#https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]

print(solution([0, 31, 24, 10, 1, 9]))
print(solution([1, 2, 3, 4, 5]))