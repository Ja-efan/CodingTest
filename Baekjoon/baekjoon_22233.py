# https://www.acmicpc.net/problem/22233
# 가희와 키워드
# Silver II

import sys
from collections import defaultdict

input = sys.stdin.readline
output = sys.stdout.write

def count_keywords(d) :
    cnt = 0
    for dd in d.values():
        cnt += sum(list(dd.values()))
    return cnt
        
def solution():
    N, M = map(int, input().split())
    
    # {맨 앞 한글자 : {단어 : 개수}}
    keywords = defaultdict(dict)
    for _ in range(N):
        keyword = input().rstrip()
        k = keyword[0]
        keywords[k][keyword] = 1
    
    # print(keywords)


    for _ in range(M):
        used_lst = list(input().rstrip().split(','))
        for used in used_lst:
            k = used[0]
            if k in keywords.keys() and used in keywords[k].keys():
                if keywords[k][used] > 0:
                    keywords[k][used] -= 1
                else :
                    continue
            else :
                continue

        # print(keywords)
        output(str(count_keywords(keywords)))        


solution()