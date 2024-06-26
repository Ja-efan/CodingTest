# https://www.acmicpc.net/problem/2178
# 미로 탐색
# Silver I

import sys
from collections import deque

inputf = sys.stdin.readline
printf = sys.stdout.write

def solution():
    N, M  = map(int, inputf().rstrip().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int,list(inputf().rstrip()))))

    def is_able(y, x)->bool:
        if 0 <= y and y < N and 0 <= x and x < M and grid[y][x]==1: return True
        else : return False 

    # print(grid)

    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt_grid = [[0 for _ in range(M)] for _ in range(N)]
    cnt_grid[0][0] = 1
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    stack = deque([(0,0)])

    while stack :
        pos = stack.popleft()
        y = pos[0]
        x = pos[1]
        visited[y][x] = True
        for dir in directions:
            dy = y + dir[0]
            dx = x + dir[1]
            if not is_able(dy, dx):
                continue
            # visited[dy][dx] = True
            if visited[dy][dx] :
                if cnt_grid[y][x] + 1 < cnt_grid[dy][dx]:
                    cnt_grid[dy][dx] = cnt_grid[y][x] + 1
                    stack.append((dy, dx))
            else :
                visited[dy][dx] = True
                cnt_grid[dy][dx] = cnt_grid[y][x] + 1
                stack.append((dy, dx))
    
    # print(cnt_grid)
    print(cnt_grid[-1][-1])

            
solution()