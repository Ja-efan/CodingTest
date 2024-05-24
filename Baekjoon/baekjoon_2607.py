# https://www.acmicpc.net/problem/2607
# 비슷한 단어
# Silver II

import sys
from collections import defaultdict

input = sys.stdin.readline
output = sys.stdout.write 

def solution():
    n = int(input())

    word_lst = []
    for _ in range(n):
        word_lst.append(input().rstrip())

    """
    비슷한 단어 : 
    1. 두 단어가 같은 구성을 갖는 경우
        '같은 구성을 갖는다.'
            - 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
            - 같은 문자는 같은 개수 만큼 있다.
    2. 한 단어에서 한 문자를 더하거나, 빼거나, 다른 문자로 바꾸어 구성이 동일한 경우
    """

    first_word = word_lst[0]
    similar_word = 0

    for word in word_lst[1:]:
        # 단어간 길이가 2이상 나는 경우 비슷한 단어일 수 없다.
        if abs(len(word) - len(first_word)) > 1:
                continue
        
        # 비교 단어에 대한 dict객체 생성
        word_dict = defaultdict(int)
        for c in word:
            word_dict[c] += 1

        # 기준 단어와 비교 단어의 길이가 동일한 경우 
        if len(word) == len(first_word):
            for w in first_word:  # 기준 단어의 각 문자에 대하여 
                if w in word and word_dict[w] > 0:  # 비교단어에 존재하고, 남은 개수가 1개 이상인 경우
                    word_dict[w] -= 1  # 개수 -1

            if sum(list(word_dict.values())) <= 1:  # word에 남은 문자가 1개 이하인 경우 문자를 제거, 추가 혹은 수정하여 비슷한 단어를 구성할 수 있다.
                similar_word += 1
                

        # 기준 단어와 비교 단어의 길이가 다른 경우 
        else :
            # 비교 단어의 길이가 더 긴 경우 
            if len(word) > len(first_word):
                for w in first_word:
                    if w in word and word_dict[w] > 0:
                        word_dict[w] -= 1
                if sum(list(word_dict.values())) == 1:  # word에 남은 문자가 1개인 경우, 해당 문자를 제거하여 비슷한 단어를 구성할 수 있다.
                    similar_word += 1

            # 기준 단어의 길이가 더 긴 경우 
            elif len(word) < len(first_word):
                for w in first_word:
                    if w in word and word_dict[w] > 0:  
                        word_dict[w] -= 1
                if sum(list(word_dict.values())) == 0:  # word에 남은 단어가 없는 경우, 기준 단어에서 한 문자를 제거하여 비슷한 단어를 구성할 수 있다.
                    similar_word += 1


    output(str(similar_word))


solution()