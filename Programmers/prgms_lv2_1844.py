# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 게임 맵 최단거리 
# DFS & BFS

def solution(maps) -> int:
    """
    게임 맵 최단거리 :
    게임 맵의 상태 maps가 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 반환.
    단, 상대팀 진영에 도착할 수 없을 때는 -1을 반환.

    Args :
    - maps : n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1이상 100이하의 자연수.
        * n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 주어지지 않는다.
        * maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타낸다.
        * 처음에 캐릭터는 게임 맵의 좌측 상단인 (1,1)위치에 있으며, 
         상대방 진영은 게임 맵의 우측 하단인 (n,m)위치에 있다.
    """

    """
    캐릭터가 (i,j)위치에 있을 때, (i-1,j), (i,j-1), (i,j+1), (i+1,j) 중 방문하지 않은 곳으로 이동 가능.
    """
    from collections import deque

    dq = deque()
    n = len(maps) # height
    m = len(maps[0]) # width 
    visited = [[0 for _ in range(m)] for _ in range(n)] # 방문 처리 배열 -> 해당 위치 까지 몇 번의 이동이 있었는지 저장 (새로운 값이 저장되어 있는 값보다 작다면 새로운 값을 입력)
    dis = [[1 for _ in range(m)] for _ in range(n)]
    dq.append((0,0))
    moves = [(0,1), (1,0), (-1,0), (0,-1)]

        
    while dq :
        i,j = dq.popleft()
        visited[i][j] = 1
        for move in moves:
            if 0<=i+move[0]<n and 0<=j+move[1]< m : # maps 범위 내에 있어야 하며, 
                if maps[i+move[0]][j+move[1]] == 1 : # 벽이 아닌 길 이어야 하고, 
                    if visited[i+move[0]][j+move[1]] == 0 : # 방문하지 않은 곳
                        visited[i+move[0]][j+move[1]] = 1
                        dq.append((i+move[0],j+move[1]))
                        curr = dis[i][j]
                        dis[i+move[0]][j+move[1]] += curr
        
    print(dis)
    return dis[-1][-1] if visited[-1][-1] == 1 else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
