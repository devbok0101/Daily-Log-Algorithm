# https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    nums = [str(i) for i in range(0,10)]
    answer = []

    for word in my_string:
        if word in nums:
            answer.append(int(word))

    answer.sort()
    return answer

def soulution2(my_string):
    nums = [str(i) for i in range(0,10)]
    return sorted([int(i) for i in my_string if i in nums])


print(soulution2("hi12392"))