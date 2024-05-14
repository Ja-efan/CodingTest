# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&problemLevel=4&contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1
# [S/W 문제해결 응용] 4일차 - 보급로
# D4
# bfs

def solution_1249():
    t = int(input())
    for i in range(1, t+1):
        matrix = []
        n = int(input())
        for _ in range(n):
            input_ = input()
            row = [int(c) for c in input_]
            matrix.append(row)

        visited = [[0 for _ in range(n)] for _ in range(n)]
        sum_matrix = [[0 for _ in range(n)] for _ in range(n)]
        stack = [(0,0)]
        direction_y = [0,1,0,-1]
        direction_x = [1,0,-1,0]
        while stack:
            y,x = stack.pop(0)
            visited[y][x] = 1 # 현재 좌표 방문처리 
            for j in range(4):
                # 다음(이동가능한) 좌표
                next_y = y + direction_y[j]
                next_x = x + direction_x[j]
                if next_x < 0 or next_x == n or next_y < 0 or next_y == n : # 다음 좌표 유효성 검사 
                    continue
                elif visited[next_y][next_x] : # 방문했던 좌표 
                    if sum_matrix[next_y][next_x] <= sum_matrix[y][x] + matrix[next_y][next_x]:
                        continue
                    else : # sum_matrix[next_y][next_x] > sum_matrix[y][x] + matrix[next_y][next_x]
                        sum_matrix[next_y][next_x] = sum_matrix[y][x] + matrix[next_y][next_x]
                        stack.append((next_y,next_x)) # 비용이 업데이트 된 좌표를 stack에 추가 
                else : # 방문하지 않은 좌표 
                    stack.append((next_y, next_x)) # 스택에 추가 
                    visited[next_y][next_x] = 1 # 방문 처리 
                    sum_matrix[next_y][next_x] = sum_matrix[y][x] + matrix[next_y][next_x] # 비용 계산

        print(f"#{i} {sum_matrix[-1][-1]}")
solution_1249()
