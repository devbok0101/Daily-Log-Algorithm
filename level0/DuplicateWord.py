# https://school.programmers.co.kr/learn/courses/30/lessons/120888


def solution(my_string):
    answer = []
    for word in my_string:
        if word not in answer:
            answer.append(word)

    return "".join(i for i in answer)


def solution2(my_string):
    return "".join(dict.fromkeys(my_string))

print(solution2("people"))
print(solution2("We are the world"))