# https://www.acmicpc.net/problem/1260
# DFS와 BFS
# Silver II

import sys
from collections import defaultdict, deque

inputf = sys.stdin.readline
printf = sys.stdout.write

def solution():

    N, M, V = map(int, inputf().rstrip().split())
    graph = defaultdict(list)

    for _ in range(M):
        v1, v2 = map(int, inputf().rstrip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)


    # dfs
    visited = [0 for _ in range(N)]
    stack = deque([V])
    visit_order = []
    while stack:
        v = stack.pop()
        if not visited[v-1]:
            visit_order.append(v)
        visited[v-1] = 1
        tmp_stack = []
        for adj in graph[v]:
            if not visited[adj-1]:
                tmp_stack.append(adj)
        stack.extend(sorted(tmp_stack, reverse=True))

    print(*visit_order, end=" ")
    print()

    # bfs 
    visited = [0 for _ in range(N)]
    dq = deque([V])
    visit_order = []
    while dq:
        v = dq.popleft()
        if not visited[v-1]:
            visit_order.append(v)
        visited[v-1] = 1
        tmp_stack = []
        for adj in graph[v]:
            if not visited[adj-1]:
                tmp_stack.append(adj)
        dq.extend(sorted(tmp_stack))
    print(*visit_order, end=" ")


solution()