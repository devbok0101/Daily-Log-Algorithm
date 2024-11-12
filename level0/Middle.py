import math


def solution(array):
    array.sort()
    index = math.floor(len(array) / 2)
    return array[index]

print(solution([9, -1, 0]))
# https://school.programmers.co.kr/learn/courses/30/lessons/120811


# sorted(array) vs array.sort()
# 전자는 원본 리스트를 변형하지 않고, 새로운 리스트 생성
# 후자는 원본 리스트를 변형함.