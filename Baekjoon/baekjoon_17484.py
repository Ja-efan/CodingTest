# https://www.acmicpc.net/problem/17484
# 진우의 달 여행(Small)
# Silver III


def solution():
    import sys

    input = sys.stdin.readline
    output = sys.stdout.write

    N, M = map(int, input().split())
    fuels = []  # NxM 크기의 지구와 달 사이의 공간 행렬
    for _ in range(N):
        fuels.append(list(map(int, input().split())))

    # 우주선이 움직일 수 있는 방향
    directions = [(1, -1), (1, 0), (1, 1)]

    # 우주선은 같은 방향으로 두번 연속 움직일 수 없다.
    pre_direction = 0
    min_fuels_lst = []
    for j in range(M):
        y = 0
        x = j

        visited = [[0 for _ in range(M)] for _ in range(N)]
        fuels_sum = [[0 for _ in range(M)] for _ in range(N)]
        stack = [(y,x, -1)]  # 어느 방향으로 움직였는지 0,1,2 로 표현. (첫 움직임은 -1로 예외)
        fuels_sum[0] = fuels[0]

        while stack:
            curr = stack.pop()
            curr_y = curr[0]
            curr_x = curr[1]
            pre_dir = curr[2]
            visited[curr_y][curr_x] = 1

            for i in range(3):
                dir = directions[i]
                next_y = curr_y + dir[0]
                next_x = curr_x + dir[1]
                next_dir = i
                if next_y == N or next_x < 0 or next_x == M or pre_dir == next_dir:
                    continue
                elif visited[next_y][next_x] and fuels_sum[next_y][next_x] > fuels_sum[curr_y][curr_x] + fuels[next_y][next_x]:
                    stack.append((next_y, next_x, next_dir))
                    visited[next_y][next_x] = 1
                    fuels_sum[next_y][next_x] = fuels_sum[curr_y][curr_x] + fuels[next_y][next_x]
                elif not visited[next_y][next_x]:
                    stack.append((next_y, next_x, next_dir))
                    visited[next_y][next_x] = 1
                    fuels_sum[next_y][next_x] = fuels_sum[curr_y][curr_x] + fuels[next_y][next_x]
                else :
                    continue
        
        min_fuels_lst.append(min(fuels_sum[-1])) 
    
    print(min_fuels_lst)



def solution2():
    import sys

    input = sys.stdin.readline
    output = sys.stdout.write

    N, M = map(int, input().split())
    fuels = []  # NxM 크기의 지구와 달 사이의 공간 행렬
    for _ in range(N):
        fuels.append(list(map(int, input().split())))

    # 우주선이 움직일 수 있는 방향
    directions = [(1, -1), (1, 0), (1, 1)]
    
    def dfs(y, x, pre_dir, min_fuel, fuel):
        if y == N-1:
            return min(min_fuel, fuel)
        
        for i in range(3):
            if i != pre_dir:
                next_y = y + directions[i][0]
                next_x = x + directions[i][1]
                if 0 <= next_y and next_y < N and  0 <= next_x and next_x < M:
                    min_fuel = dfs(next_y, next_x, i, min_fuel, fuel+fuels[next_y][next_x])
        return min_fuel
    

    min_fuel = 600
    for j in range(M):
        min_fuel = min(dfs(0, j, -1, min_fuel, fuels[0][j]), min_fuel)

    print(min_fuel)


def solution3():
    import sys

    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dir = {1: (1, -1), 2: (1, 0), 3: (1, 1)}

    def dfs(i, j, now_dir, min_fuel, fuel):
        if i == n-1:
            return min(min_fuel, fuel)
        for k in range(1, 4):
            if now_dir != k:
                if 0 <= i+dir[k][0] < n and 0 <= j+dir[k][1] < m:
                    min_fuel = dfs(i+dir[k][0], j+dir[k][1], k, min_fuel, fuel+grid[i+dir[k][0]][j+dir[k][1]])
        return min_fuel

    min_fuel = int(sys.maxsize)
    for i in range(m):
        min_fuel = min(dfs(0, i, 0, min_fuel, grid[0][i]), min_fuel)

    print(min_fuel)

solution2()