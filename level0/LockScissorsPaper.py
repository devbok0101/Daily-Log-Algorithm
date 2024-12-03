#https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    answers = {"2": "0",
              "0": "5",
              "5": "2",
              }

    return ''.join(answers[hand] for hand in rsp)


print(solution("2"))