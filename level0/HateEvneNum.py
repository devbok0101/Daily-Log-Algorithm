#https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    answer = []

    for i in range(1, n + 1):
        if i % 2 != 0:
            answer.append(i)

    return answer

print(solution(1))