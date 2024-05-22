# https://www.acmicpc.net/problem/1205
# 등수 구하기 
# Silver IV

import sys

input = sys.stdin.readline

def solution():
    """
    P : 랭킹 리스트에 올라 갈 수 있는 점수의 개수 (10 <= P <= 50)
    N : 현재 랭킹 리스트에 있는 점수의 개수 (0 <= N <= P)
    """

    N, S, P = map(int, input().rstrip().split())
    if N == 0:
        print(1)
        return 

    scores = list(map(int, input().rstrip().split()))

    if scores[-1] >= S and N == P:
        print(-1)
        return 
    
    ranking = [[0,0] for _ in range(N)]

    ranking_dict = {
        scores[0] : 1
    }
    for i in range(1, N):
        if scores[i] == scores[i-1]:
            continue
        ranking_dict[scores[i]] = i+1
    
    ranking_dict = dict(sorted(ranking_dict.items(), key=lambda x:x[1]))

    for item in ranking_dict.items():
        score = item[0]
        rank = item[1]

        if S >= score:
            print(rank)
            break
        # elif S > score:
        #     print(rank)

def solution2():
    N, S, P = map(int, input().rstrip().split())
    if N == 0 :
        print(1)
        return
    scores = list(map(int, input().rstrip().split()))

    if N == P and scores[-1] >= S :
        print(-1)
        return
    
    ts_rank = 0
    for i in range(N):
        if S < scores[i] :
            continue
        elif S == scores[i]:
            continue
        elif S > scores[i]:
            if S == scores[i-1]:
                ts_rank = i
            else :
                ts_rank = i+1
            break
        else :
            ts_rank = N+1
    print(ts_rank)

def solution3():
    n, s, p = map(int, input().rstrip().split())
    if n == 0 :
        print(1)
        return
    else :
        scores = list(map(int, input().rstrip().split()))  # 점수는 내림차순을 정렬되어있다.
        scores_rank = dict()
        for i in range(n):
            scores_rank[scores[i]] = i+1
        
        if n == p and scores[-1] >= s:  # 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮은 경우 
            print(-1)
            return 
        
        scores_rank = sorted(scores_rank.items(), key=lambda x:x[1])
        # print(scores_rank)

        ts_rank = 0
        # new_scores = [0 for _ in range(P)]
        for j in range(len(scores_rank)):
            score = scores_rank[j][0]
            rank = scores_rank[j][1]
            if score > s :
                if j + 1 == n and ts_rank == 0:
                    ts_rank = n+1
                continue
            elif score <= s:
                ts_rank = rank
                break

        print(ts_rank)

def solution4():
    n, s, p = map(int, input().rstrip().split())
    if n == 0:
        print(1)
        return 
    
    scores = list(map(int, input().rstrip().split()))
    if n == p and scores[-1] >= s:
        print(-1)
        return 
    
    scores_rank = dict()  # [점수, 순위] 쌍을 담는 dict 객체

    for i in range(n):
        if scores[i] not in scores_rank.keys():
            scores_rank[scores[i]] = i+1  # 점수:순위 쌍을 scores_rank 객체에 저장

    scores_rank_keys = list(scores_rank.keys())
    scores_rank_keys.sort(reverse=True)

    ts_rank = 0
    for i, k in enumerate(scores_rank_keys):
        if s < k:
            if n < p and k == min(scores_rank_keys):
                ts_rank = n+1
                break

        elif s >= k :
            ts_rank = scores_rank[k]
            break
    
    print(ts_rank)

    
solution4()