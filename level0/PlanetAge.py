# https://school.programmers.co.kr/learn/courses/30/lessons/120834
from collections import defaultdict


def solution(age):
    spell = create_spell_map()
    return ''.join(spell[int(num)] for num in str(age))


def create_spell_map():
    ans = defaultdict()
    spell = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in range(0, 10):
        ans[i] = spell[i]
    return spell


print(solution(23))
