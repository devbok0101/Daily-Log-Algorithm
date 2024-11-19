def solution(num_list):
    answer = []
    num_len = len(num_list) - 1
    while num_len != -1:
        answer.append(num_list[num_len])
        num_len -= 1

    return answer


print(solution([1, 2, 3, 4, 5]))
