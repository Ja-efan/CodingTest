# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기 
# 1018
# import numpy as np
# import copy 
def solution():
    # 사용자 입력 부분 
    n, m = map(int, input().split(" "))
    maps = []
    for i in range(n):
        row = input()
        maps.append(list(row))
    # print(maps)
    
    # 자를 수 있는 위치 : (0,0) ~ (n-8, m-8)
    counts = []
    for i in range(n-8+1):
        for j in range(m-8+1):
            # start with 'B'
            new_maps = [[0 for _ in range(8)] for _ in range(8)]
            count = 0
            new_maps[0][0] = 'B'
            curr = new_maps[0][0]
            if curr != maps[i][j] :
                count += 1
            for k in range(8):
                for l in range(8):
                    if k == 0 and l == 0 :
                        continue
                    if curr == maps[i+k][j+l]:
                            count += 1
                            if maps[i+k][j+l] == "B":
                                new_maps[k][l] = "W"
                            else :
                                new_maps[k][l] = "B"
                    else :
                        new_maps[k][l] = maps[i+k][j+l]
                    curr = new_maps[k][l]
                    if l == 7:
                        if curr == "W" :
                            curr = 'B'
                        else : 
                            curr = "W"  
            counts.append(count)
            # start with 'W'
            new_maps = [[0 for _ in range(8)] for _ in range(8)]
            count = 0
            new_maps[0][0] = 'W'
            curr = new_maps[0][0]
            if curr != maps[i][j] :
                count += 1
            for k in range(8):
                for l in range(8):
                    if k == 0 and l == 0 :
                        continue
                    if curr == maps[i+k][j+l]:
                            count += 1
                            if maps[i+k][j+l] == "B":
                                new_maps[k][l] = "W"
                            else :
                                new_maps[k][l] = "B"
                    else :
                        new_maps[k][l] = maps[i+k][j+l]
                    curr = new_maps[k][l]
                    if l == 7:
                        if curr == "W" :
                            curr = 'B'
                        else : 
                            curr = "W"  

            print(count)
            counts.append(count)

    return min(counts)
                

print(solution())

