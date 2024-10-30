from typing import List


class Solution:
    def solution(relation):
        col_len = len(relation[0])
        row_len = len(relation)

        candidate_keys = []
        # 모든 속성 조합별로 후보키 적합성 검사
        for cols in range(1, 1 << col_len):
            minimality = True
            row_set = set()
            # 기존 후보키들과 비교해서 최소성 검사 수행
            for key in candidate_keys:
                if key & cols == key:
                    minimality = False
                    break
            # 최소성이 위반되면 다음 속성 조합 후보키 검사 진행
            if not minimality:
                continue

            # 속성 조합을 기반으로 유일성 검사
            for r in range(row_len):
                row_str = ""
                for c in range(col_len):
                    print("cols : " + str(cols) + "  c : " + str(c))
                    if cols & (1 << c):
                        row_str += " " + relation[r][c]
                row_set.add(row_str)
            # 튜플간 중복이 없으면, 해당 속성 조합 후보키 선정
            if len(row_set) == row_len:
                candidate_keys.append(cols)

        answer = len(candidate_keys)
        return answer



        return answer


print(Solution.solution(
    [
     ["100", "ryan", "music", "2"],
     ["200", "apeach", "math", "2"],
     ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"],
     ["500", "muzi", "music", "3"],
     ["600", "apeach", "music", "2"]
     ]))
