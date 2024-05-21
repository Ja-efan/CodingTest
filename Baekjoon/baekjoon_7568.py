# https://www.acmicpc.net/problem/7568
# 덩치 
# Silver V

import sys 

input = sys.stdin.readline
def solution():
    N = int(input().rstrip())
    dict_ = dict()
    for i in range(N):
        x, y = map(int, input().rstrip().split())
        dict_[i] = [x,y,x+y]

    dict_ = list(sorted(dict_.items(), key = lambda x:x[1][2], reverse=True))
    print(dict_)


    rank_lst = [0 for _ in range(N)]
    for j in range(N):
        jth = dict_[j]
        if j == 0 :
            rank_lst[jth[0]] = 1
        else :
            pre = dict_[j-1]
            if pre[1][0] > jth[1][0] and pre[1][1] > jth[1][1]:
                rank_lst[jth[0]] = j+1
            else :
                rank_lst[jth[0]] = rank_lst[pre[0]]

    print(*rank_lst, sep=" ")
    # result = ""
    # for r in rank_lst:
    #     result += str(r)+" "

    # print(result)


def solution2():
    """
    N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 '큰 덩치'의 사람의 수로 정해진다.
    '덩치가 더 크다' -> 몸무게와 키가 모두 자신보다 크다.
    """
    N = int(input().rstrip())

    dungchi = dict()
    for i in range(N):
        x, y = map(int, input().rstrip().split())
        dungchi[i] = (x,y)

    bigger_list = [0 for _ in range(N)]

    for item in dungchi.items():
        weight = item[1][0]
        height = item[1][1]
        bigger = 0
        for j, k in enumerate(dungchi.keys()):
            if item[0] == k:
                continue
            else :
                if dungchi[k][0] > weight and dungchi[k][1] > height:
                    bigger += 1
        

        bigger_list[item[0]] = bigger

    result = ""
    for r in bigger_list:
        result += str(r+1) + " "

    print(result)

solution2()