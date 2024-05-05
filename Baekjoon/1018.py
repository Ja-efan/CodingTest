# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기 
# 1018
# import numpy as np
import copy 
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
            new_maps = [[0 for _ in range(8)] for _ in range(8)]
            # print(f"start index : ({i,j})")
            count = 0 
            curr = maps[i][j] 
            # curr_maps = maps[i:i+8][j:j+8]
            # print(np.stack(curr_maps, axis=1))
            for k in range(8):
                for l in range(8):
                    if k == 0 and l == 0 :
                        new_maps[i+k][j+l] = curr
                        continue
                    if curr == maps[i+k][j+l]:
                        count += 1
                        if maps[i+k][j+l] == "B":
                            new_maps[i+k][j+l] = "W"
                        else :
                            new_maps[i+k][j+l] = "B"
                    curr = maps[i+k][j+l]
                    if l == 7:
                        if curr == "W" :
                            curr = 'B'
                        else : 
                            curr = "W"
            print(count)
            counts.append(count)

    return min(counts)
                

print(solution())

