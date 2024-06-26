# https://www.acmicpc.net/problem/2606
# 바이러스
# Silver III

import sys
from collections import deque, defaultdict

inputf = sys.stdin.readline
printf = sys.stdout.write

def solution():
    
    computers = int(inputf().strip())
    conn = int(inputf().strip())
    connections = defaultdict(list)

    for i in range(conn):
        a, b = map(int, input().strip().split())
        connections[a].append(b)
        connections[b].append(a)

    # print(connections)

    visited = [False for _ in range(computers)]
    cnt = 0
    stack = [1]
    while stack:
        curr_pc = stack.pop()
        for next_pc in connections[curr_pc]:
            if visited[next_pc-1]:
                continue
            visited[next_pc-1] = True
            stack.append(next_pc)
            cnt += 1

    if cnt == 0:
        print(cnt)
    else :
        print(cnt-1)

solution()