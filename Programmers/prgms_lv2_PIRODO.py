# 87946 
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k:int, dungeons:list) -> int :
    """
    피로도 : 
    '최소 필요 피로도' : 던전을 탐험하기 위해 필요한 최소 피로도
    '소모 피로도' : 던전을 탐험한 후 실제 소모되는 피로도 
    예를 들어, 최소 필요 피로도가 80, 소모 피로도가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도가 80이상 이어야 하며,
    던전을 탐험한 후에는 피로도 20이 소모된다. 

    Args : 
    - k : 유저의 현재 피로도, 1 <= k <= 5000 자연수 
    - dungeons : 던전 별 '최소 필요 피로도'와 '소모 피로도'가 담긴 2차원 배열, 
        던전의 개수(행의 개수)는 1개 이상 8개 이하,
        열의 개수는 2개,
        각 행은 ['최소 필요 피로도', '소모 피로도']로 구성,
        1<= 소모 피로도 <= 최소 필요 피로도 <= 1000 자연수,
        서로 다른 던전(다른 행)의 '최소 필요 피로도'와 '소모 피로도'가 동일할 수 있음.

    Returns : 유저가 탐험할 수 있는 최대 던전 수 

    ! 각 던전은 하루에 한 번씩 탐험 가능.
    """
    from itertools import permutations

    # 던전의 개수
    num_dungeons = len(dungeons)
    id = []
    for i in range(num_dungeons):
        id.append(i)
    
    # 모든 경우의 수를 담고 있음  len(trial) = num_dungeons! 
    trial = list(permutations(id, len(id)))

    answer = 0
    for t in trial :
        cnt = 0
        pirodo = k 
        for i in t:
            if pirodo >= dungeons[i][0] and pirodo - dungeons[i][1] > 0:
                pirodo -= dungeons[i][1]
                cnt += 1
            else :
                break
        if cnt > answer:
            answer = cnt
    return answer 


    


# test case 
print(solution(80,[[80,20],[50,40],[30,10]])) # 3

