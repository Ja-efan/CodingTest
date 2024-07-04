# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZBIg6i6E1gDFAUu&contestProbId=AXuARWAqDkQDFARa&probBoxId=AZBNDpl6hGQDFAUu&type=USER&problemBoxTitle=%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98+Track+%28%EB%82%9C%EC%9D%B4%EB%8F%84+%EC%A4%91%29&problemBoxCnt=3
# 파리퇴치
# D2
# SSAFY 12기 사전학습 

# import sys 

# inputf = sys.stdin.readline
# printf = sys.stdout.write

def solution():
    T = int(input())
    for t in range(T):
        N, M = map(int, input().rstrip().split())
        grid = []
        for _ in range(N):
            grid.append(list(map(int, input().rstrip().split())))

        def is_able(y,x):
            if 0 <= y and y < N and 0 <= x and x < N: return True
            else : return False 

    
        max_flies = 0
        dir1 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dir2 = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

        for i in range(N):
            for j in range(N):
                # dir1 : + 형태 분사 
                y = i
                x = j
                tmp_flies = grid[y][x]
                for p in range(1, M):
                    for d in dir1:
                        dy = y + d[0]*p 
                        dx = x + d[1]*p
                        if is_able(dy, dx):
                            tmp_flies += grid[dy][dx]
                if max_flies < tmp_flies :
                    max_flies = tmp_flies

                # dir2 : x 형태 분사
                tmp_flies = grid[y][x]
                for p in range(1, M):
                    for d in dir2:
                        dy = y + d[0]*p
                        dx = x + d[1]*p
                        if is_able(dy, dx):
                            tmp_flies += grid[dy][dx]
                if max_flies < tmp_flies:
                    max_flies = tmp_flies

        print(f"#{t+1} {max_flies}")


solution()