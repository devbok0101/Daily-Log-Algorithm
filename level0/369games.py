#https://school.programmers.co.kr/learn/courses/30/lessons/120891

def isNumIn369(num):
    return num == 3 or num == 6 or num == 9


def solution(order):
    numbers = list(map(int, str(order)))
    answer = 0
    for num in numbers:
        if isNumIn369(int(num)):
            answer += 1
    return answer

print(solution(29423))