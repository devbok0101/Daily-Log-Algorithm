#https://school.programmers.co.kr/learn/courses/30/lessons/120837


def solution(hp):
    if hp == 0:
        return 0
    generalAntCount = hp // 5
    remain = hp % 5
    if remain == 0:
        return generalAntCount

    if remain > 0:
        armyAntCount = remain // 3
        lastRemain = remain % 3

        if lastRemain > 0:
            return generalAntCount + armyAntCount + lastRemain
        else:
            return generalAntCount + armyAntCount

print(solution(1000))
print(solution(24))
print(solution(999))