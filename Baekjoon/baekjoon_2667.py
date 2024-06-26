# https://www.acmicpc.net/problem/2667
# 단지번호붙이기
# Silver I

import sys

inputf = sys.stdin.readline
printf = sys.stdout.write

def solution():

    N = int(inputf().strip())

    grid = []

    for _ in range(N):
        grid.append(list(map(int, list(inputf().rstrip()))))

    # print(grid)

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    def is_able(y, x):
        if 0 <= y and y < N and 0 <= x and x < N and grid[y][x] == 1 : return True
        else : return False
    
    cnt_list = []
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i, j)]
                cnt = 0
                while stack :
                    curr = stack.pop()
                    cnt += 1
                    curr_y = curr[0]
                    curr_x = curr[1]
                    visited[curr_y][curr_x] = True
                    for dir in directions:
                        next_y = curr_y + dir[0]
                        next_x = curr_x + dir[1]
                        if not is_able(next_y, next_x):
                            continue 
                        if not visited[next_y][next_x]:
                            visited[next_y][next_x] = True 
                            stack.append((next_y, next_x))

                cnt_list.append(cnt)

    cnt_list.sort()    
    print(len(cnt_list))
    for cnt in cnt_list:
        print(cnt)


solution()