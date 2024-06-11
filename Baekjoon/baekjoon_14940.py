# https://www.acmicpc.net/problem/14940
# 쉬운 최단거리
# Silver I

import sys
from collections import deque

inputf = sys.stdin.readline
prinft = sys.stdout.write

def solution():
    n, m = map(int, inputf().split())
    mapp = []

    target = (-1,-1)  # 목표지점 좌표 
    for i in range(n):
        tmp = list(map(int, inputf().rstrip().split()))
        mapp.append(tmp)
        if 2 in tmp:  # 목표 지점 있는 경우 
            target = (i, tmp.index(2))  # 목표지점 좌표 설정
    
    # 방문 체크 리스트
    visited = [[-1 for _ in range(m)] for _ in range(n)]

    def bfs(src:tuple):
        
        directions = [(-1,0), (0, -1), (1, 0), (0, 1)]

        dq = deque([src])
        visited[src[0]][src[1]] = 0
        while dq:
            curr = dq.popleft()
            y = curr[0]
            x = curr[1]
            
            for dir in directions:
                ny = y + dir[0]
                nx = x + dir[1]
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue

                if mapp[ny][nx] == 0:
                    visited[ny][nx] = 0 

                elif visited[ny][nx] == -1 and mapp[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    dq.append((ny,nx))
                

    bfs(target)
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 0:
                visited[i][j] = 0


    for col in visited:
        print(*col, end=" ")
        print()




solution()