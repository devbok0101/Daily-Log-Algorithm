#https://school.programmers.co.kr/learn/courses/30/lessons/120837


def solution(hp):
    answer = hp // 5
    hp %= 5
    answer += hp // 3
    hp %= 3
    answer += hp // 1
    return answer

print(solution(1000))
print(solution(24))
print(solution(999))