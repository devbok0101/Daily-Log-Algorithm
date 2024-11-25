# https://school.programmers.co.kr/learn/courses/30/lessons/120834
from collections import defaultdict


def solution(age):
    answer = ''
    ans = defaultdict()
    spell = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    for i in range(0, 10):
        ans[i] = spell[i]

    for num in str(age):
        answer += spell[int(num)]

    return answer


print(solution(23))
