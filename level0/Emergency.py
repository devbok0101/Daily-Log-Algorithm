# https://school.programmers.co.kr/learn/courses/30/lessons/120835
from collections import defaultdict


def solution(emergency):
    dic = create_priority_dic(emergency)

    answer = []
    for num in emergency:
        answer.append(dic[num])
    return answer


def create_priority_dic(emergency):
    reverse_list = emergency[:]
    reverse_list.sort(reverse=True)
    dic = defaultdict()
    priority = 1
    for num in reverse_list:
        dic[num] = priority
        priority += 1
    return dic


print(solution([3, 76, 24]))
