# https://www.acmicpc.net/problem/3758
# KCPC
# Silver II

import sys 
from collections import defaultdict

input = sys.stdin.readline
output = sys.stdout.write

def solution():
    """
    문제에 대해 제출한 풀이 중 최고 점수가 해당 문제의 최종 점수가 된다. 
    팀의 최종 점수 : 각 문제에 대해 받은 점수의 총합 
    팀의 최종 순위 : 더 높은 점수를 받은 팀의 수 + 1
    동점자 처리 
        1. 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다.
        2. 최종 점수도 같고, 풀이 제출 횟수도 동일한 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 더 높다.
    """
    
    """
    필요한 정보 
    팀
        문제 당 제출 횟수
        문제 당 최고 점수 
        전체 문제에 대한 점수 총합

    """

    T = int(input())  # 테스트 케이스 개수 
    for _ in range(T):
        n, k, t, m = map(int, input().split())

        # logs에는 (팀 ID, 문제번호, 획득한 점수)로 구성된 튜플이 저장된다.
        logs = []
        for _ in range(m):
            logs.append(tuple(map(int, input().split())))

        dict_score = defaultdict(lambda: defaultdict(int))  # {team ID : {문제 번호 : 최종 점수}}
        dict_submit = defaultdict(lambda:[0,0])  # {team ID : [전체 제출 횟수, 마지막 제출 횟수]}
        
        for i, log in enumerate(logs): 
            tid, j, s = log
            dict_submit[tid][0] += 1
            dict_submit[tid][1] = i
            if dict_score[tid][j] < s : 
                dict_score[tid][j] = s

        dict_team = dict()  # {team ID : 최종 점수(점수 총합), 제출 횟수, 마지막 제출(로그 인덱스)}
        for tid, scores in dict_score.items():
            total_score = sum(list(scores.values()))
            num_submits = dict_submit[tid][0]
            last_submit = dict_submit[tid][1]
            dict_team[tid] = [total_score, num_submits, last_submit]

        # 동점자 처리에 맞게끔 정렬 
        dict_team_sorted = dict(sorted(dict_team.items(), key=lambda x : (-x[1][0], x[1][1], x[1][2]))) 
        rank = list(dict_team_sorted.keys())
        my_rank = rank.index(t)+1 

        output(str(my_rank)+'\n')


solution()
