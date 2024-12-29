# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    answer = array[0]
    for number in array:
        if abs(n - answer) > abs(n - number):
            answer = number
        if abs(n - answer) == abs(n - number):
            answer = min(answer, number)
    return answer

def solution1(array, n):
    return min(array, key = lambda x : (abs(n - x), x))

print(solution1([3, 10, 28], 20))
print(solution1([4, 7], 1))
print(solution1([10, 11, 12], 13))