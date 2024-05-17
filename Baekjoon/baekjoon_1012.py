# https://www.acmicpc.net/problem/1012
# 유기농 배추
# silver II

def solution():
    t = int(input())  # 사용자 입력, 테스트 케이스 개수
    for tc in range(1, t+1):
        m, n, k = map(int, input().split())  # 사용자 입력, m:가로길이(width), n:세로길이(height), k:배추의 개수
        # bat = [[0 for _ in range(m)] for _ in range(n)]  # 배추밭 그리드
        poses = []
        around = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for _ in range(k):
            x, y = map(int, input().split())  # 배추가 심어진 위치 좌표
            poses.append((y, x))
            # bat[y][x] = 1  # 배추 표시
        visited = [[0 for _ in range(m)] for _ in range(n)]  # 방문 표시 배열
        warms = 0
        while poses:
            pos = poses.pop()
            i = pos[0]
            j = pos[1]
            if visited[i][j]:
                continue
            stack = [(i, j)]
            while stack:
                coord = stack.pop()
                h, w = coord[0], coord[1]
                visited[h][w] = 1
                for a in around:
                    ah = h + a[0]
                    aw = w + a[1]
                    if (ah, aw) in poses and not visited[ah][aw]:
                        visited[ah][aw] = 1
                        stack.append((ah, aw))
            warms += 1
        print(warms)


solution()

