def solution(my_string, target):

    start, last = 0, len(target)

    for st in range(my_string):
        if st == target[start]:
            start += 1


    return 0


print(solution("banana", "ana"))