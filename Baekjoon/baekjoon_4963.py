# https://www.acmicpc.net/problem/4963
# 섬의 개수
# Silver II
"""
IDEA :
    DFS로 순회
    현재 위치 기준으로 8방면에 대해 섬이 있는지 확인
    around = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
"""
def solution():
    while True:
        shape = list(map(int, input().split()))
        # print(shape)
        w = shape[0]
        h = shape[1]
        if w == 0 and h == 0:
            break
        map_ = []
        around = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        for _ in range(h):
            map_.append(list(map(int, input().split())))
        visited = [[0 for _ in range(w)] for _ in range(h)]
        stack = []
        islands = 0
        for i in range(h):
            for j in range(w):
                if map_[i][j] == 1 and not visited[i][j]:
                    stack.append((i, j))
                    visited[i][j] = 1
                    while stack:
                        coord = stack.pop()
                        x = coord[1]
                        y = coord[0]
                        visited[y][x] = 1
                        for a in around:  # len(around) : 8
                            ax = x + a[1]
                            ay = y + a[0]
                            if ax < 0 or ax == w or ay < 0 or ay == h or map_[ay][ax] == 0:
                                continue
                            elif map_[ay][ax] == 1 and not visited[ay][ax]:
                                stack.append((ay, ax))
                    islands += 1

        print(islands)

def solution2():
    while 1:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        map_ = []
        for _ in range(h):
            map_.append(list(map(int, input().split())))
        visited = [[0 for _ in range(w)] for _ in range(h)]
        islands = 0
        around = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        for i in range(h):
            for j in range(w):
                if map_[i][j] == 0:
                    continue
                elif map_[i][j] == 1 and not visited[i][j]:
                    stack = [(i, j)]
                    while stack:
                        coord = stack.pop()
                        y = coord[0]
                        x = coord[1]
                        visited[y][x] = 1
                        for a in around:
                            ay = y + a[0]
                            ax = x + a[1]
                            if ax < 0 or ax == w or ay < 0 or ay == h:
                                continue
                            elif map_[ay][ax] == 0:
                                continue
                            elif visited[ay][ax] == 1:
                                continue
                            else:
                                visited[ay][ax] = 1
                                stack.append((ay, ax))
                    islands += 1
        print(islands)


solution2()

