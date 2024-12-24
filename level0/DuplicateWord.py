# https://school.programmers.co.kr/learn/courses/30/lessons/120888


def solution(my_string):
    answer = []
    for word in my_string:
        if word not in answer:
            answer.append(word)

    return "".join(i for i in answer)


print(solution("people"))
print(solution("We are the world"))