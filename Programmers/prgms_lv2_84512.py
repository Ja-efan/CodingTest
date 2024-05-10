# https://school.programmers.co.kr/learn/courses/30/lessons/84512#qna
# 모음사전

from itertools import product
def solution(word:str) -> int :
    moeum = ['A', 'E', 'I', 'O', 'U']
    moeum_list = []
    for i in range(1,6):
        for j in product(moeum, repeat=i):
            moeum_list.append(j)
    # print(moeum_list)

    moeum_list.sort()
    for i,m in enumerate(moeum_list):
        m = ''.join(m)
        if m == word :
            return i +1
        



print(solution("AAAAE"))