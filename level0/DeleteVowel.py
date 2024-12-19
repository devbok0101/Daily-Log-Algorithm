# https://school.programmers.co.kr/learn/courses/30/lessons/120849?language=python3

def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for word in my_string:
        if word in vowel:
            continue
        else:
            answer += word
    return answer


def solution2(my_string):
    return "".join([i for i in my_string if i not in "aeiou"])


print(solution2("bus"))