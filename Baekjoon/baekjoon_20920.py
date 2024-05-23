# https://www.acmicpc.net/problem/20920
# 영단어 암기는 괴로워
# Silver III

import sys
from collections import Counter, defaultdict

input = sys.stdin.readline
output = sys.stdout.write

def solution():
    """
    1. 자주 나오는 단어일수록 앞에 배치
    2. 해당 단어의 길이가 길수록 앞에 배치
    3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
    길이가 M이상인 단어들만 외우려고 함.
    """

    N, M = map(int, input().rstrip().split())

    words = []
    for i in range(N):
        word = input().rstrip()
        if len(word) >= M:  # 길이가 M이상인 단어들만 선택
            words.append(word)

    word_counter = Counter(words)

    words_set = set(words)
    # print(words_set)

    my_dict = dict()
    for w in words_set:
        length = len(w)
        count = word_counter[w]
        my_dict[w] = (count, length)
    
    # 단어 순서를 만족 시키기 위해 
    # 단어의 출현 빈도와 길이에 -를 붙여 음수로 변환 후 오름차순으로 정렬.
    my_dict = dict(sorted(my_dict.items(), key = lambda x:(-x[1][0], -x[1][1], x[0])))
    
    # print(my_dict.keys())
    for w in my_dict.keys():
        output(w+'\n')


solution()



