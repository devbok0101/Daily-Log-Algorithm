# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def combination_recursive(balls, share):
    if share == 0 or balls == share:
        return 1
    return combination_recursive(balls - 1, share - 1) + combination_recursive(balls - 1, share)


def solution(balls, share):
    return combination_recursive(balls, share)


#print(solution(3, 2))
print(solution(5, 3))
