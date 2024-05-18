# https://www.acmicpc.net/problem/1359
# 복권
# silver IV

def solution():
    N, M, K = map(int, input().split())
    """
    N개의 숫자 중에서 M개를 고른 뒤, 적어도 K개가 같을 확률
    """
    from itertools import combinations
    comb = list(combinations(range(N), M))  # N개 중 M개를 고르는 조합. N_C_M
    comb2 = list(combinations(range(N), M))

    result = 0  # K개 이상 동일한 숫자가 존재하는 조합의 개수
    for i in range(len(comb)):
        jimin = comb[i]  # 지민이가 고른 번호들
        for j in range(len(comb2)):
            lotto = comb2[j]  # 주최 측에서 고른 번호
            cnt = 0  # 조합마다 동일한 숫자 개수
            for k in range(M):  # 고른 숫자 개수 만큼 반복
                for l in range(M):
                    if jimin[k] == lotto[l]:  # 지민이가 고른 숫자와 주최측에서 고른 숫자가 동일한 경우
                        cnt += 1  # cnt += 1
            if cnt >= K:  # 동일한 숫자 개수가 K개 이상인 경우
                result += 1

    print(result/len(comb)**2)  # 전체 가능한 경우의 수 중에 K개 이상 동일한 숫자가 존재하는 확률


solution()