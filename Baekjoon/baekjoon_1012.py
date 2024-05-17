# https://www.acmicpc.net/problem/1012
# 유기농 배추
# silver II

def solution():
    t = int(input())  # 사용자 입력, 테스트 케이스 개수
    for tc in range(1, t+1):
        """
        사용자 입력, 
        m : 가로 길이(width), 
        n : 세로 길이(height), 
        k : 배추의 개수
        """
        m, n, k = map(int, input().split())
        poses = []  # 배추가 심어진 좌표를 담을 리스트
        around = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 벌레가 이동 가능한 경로
        for _ in range(k):
            x, y = map(int, input().split())  # 배추가 심어진 위치 좌표
            poses.append((y, x))

        visited = [[0 for _ in range(m)] for _ in range(n)]  # 방문 표시 배열
        warms = 0  # 필요한 벌레 수
        while poses:  # 배추 남은 동안 반복
            pos = poses.pop()  # 좌표 하나 pop
            i = pos[0]
            j = pos[1]
            if visited[i][j]:  # 방문했던 위치라면 continue
                continue
            stack = [(i, j)]  # dfs를 위한 stack
            while stack:  # stack이 비어있지 않는 동안 반복
                coord = stack.pop()  # 좌표 하나 pop
                h, w = coord[0], coord[1]
                visited[h][w] = 1  # 해당 좌표 방문 표시
                for a in around:  # 벌레 이동 가능 경로에 대해서
                    ah = h + a[0]
                    aw = w + a[1]
                    if (ah, aw) in poses and not visited[ah][aw]:
                        # 벌레 이동 가능 경로에 배추가 심어져 있고, 방문하지 않은 위치라면
                        visited[ah][aw] = 1  # 방문 처리
                        stack.append((ah, aw))  # stack에 추가
            warms += 1
        print(warms)


solution()

