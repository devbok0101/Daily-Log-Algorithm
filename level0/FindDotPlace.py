#https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):

    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 < dot[1]:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    else:
        return 4

print(solution([2,4]))