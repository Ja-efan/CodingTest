# https://www.acmicpc.net/problem/9017
# 크로스 컨트리
# Silver III

import sys
from collections import defaultdict

input = sys.stdin.readline
# output = sys.stdin.write

def solution():
    t = int(input().rstrip())

    for tc in range(1, t+1):
        n = int(input().rstrip())
        rank = list(map(int, input().rstrip().split()))

        # 팀:[등수]의 구조를 갖는 dict 객체
        dict_ = defaultdict(list)
        for i in range(n):
            dict_[rank[i]].append(i+1)
        
        print(dict_)

        qualified = dict()
        for k, v in dict_.items():
            if len(v) < 6:
                # unqualified.append(k)
                continue
            else :
                sorted_v = sorted(v)
                qualified[k] = sorted_v
                team_score = sum(sorted_v[:4])
                qualified[k].append(team_score)

        print(qualified)

        qualified_sorted_lst = list(sorted(qualified, key=lambda x:(x[1][-1], x[1][4])))

        print(qualified_sorted_lst)
                

def solution2():
    from collections import Counter, defaultdict

    t = int(input().rstrip())
    for tc in range(1, t+1):
        n = int(input())
        rank = list(map(int, input().rstrip().split()))
        counter = Counter(rank)
        print(counter)

        qualified_rank = []
        qualified = defaultdict(list)
        for i in range(n):
            if counter[rank[i]] < 6:
                continue
            else :
                qualified_rank.append(rank[i])
                qualified[rank[i]].append(len(qualified_rank))
        # print(qualified_rank)
        # print(qualified)

        for team, scores in qualified.items():
            scores.append(sum(scores[:4]))
        # print(qualified)

        sorted_qualified = sorted(qualified.items(), key=lambda x:(x[1][-1], x[1][4]))
        # print(sorted_qualified)

        print(sorted_qualified[0][0])

solution2()


                
        
        




