# https://www.acmicpc.net/problem/8979
# 올림픽 
# Silver V 

def solution():
    """
    1. 금메달 수가 더 많은 나라
    2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
    3. 금,은메달 수가 모두 같으면 동메달 수가 더 많은 나라 
    4. 금,은,동 메달 수가 모두 같으면 공동순위를 갖는다.
    등수는 '자신 보다 더 잘한 나라의 수' + 1 로 정한다.
    즉, 1등(A 국가), 공동 2등(B,C 국가) 라면 D 국가는 4등이 된다.
    """

    N, K = map(int, input().split())  # N : 국가의 수 , K : 등수를 알고 싶은 국가 
    """
    key : value -> country : medals 
    ex) 1 : [2, 1, 0] # gold, silver, bronze 
    """
    medals = dict()
    for i in range(1, N+1):
        C, G, S, B = map(int, input().split())
        medals[C] = [G,S,B]
    
    sorted_medals = sorted(medals.items(), key = lambda x:(x[1][0], x[1][1], x[1][2]), reverse=True)
    # print(sorted_medals)
    pre_medals = []
    rank_list = [0 for _ in range(N+1)]
    for i in range(N):
        item = sorted_medals[i]

        if i == 0 :
            # pre_medals = item[1]
            rank_list[item[0]] = i+1
            
        else :
            if item[1] == sorted_medals[i-1][1]:
                rank_list[item[0]] = rank_list[sorted_medals[i-1][0]]
            else :
                rank_list[item[0]] = i+1
    
    print(rank_list[K])


solution()