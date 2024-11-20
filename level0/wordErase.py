# https://school.programmers.co.kr/learn/courses/30/lessons/120826

def solution(my_string, letter):
    answer = ''

    for word in my_string:
        if letter == word:
            continue
        else:
            answer += word

    return answer


print(solution("abete", "e"))