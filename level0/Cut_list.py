# https://school.programmers.co.kr/learn/courses/30/lessons/120833

def solution(numbers, num1, num2):
    return numbers[num1: num2 + 1]


print(solution([1, 2, 3, 4, 5], 1, 3))
