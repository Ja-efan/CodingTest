# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기
# Silver II
from collections import defaultdict


def solution():
    N = int(input())
    tree = defaultdict(list)  # 기본 값으로 리스트를 가지는 딕셔너리 생성
    for _ in range(N - 1):
        i, j = map(int, input().split())
        tree[i].append(j)  # 각 노드를 키로 가지는 연결 리스트로 트리 표현
        tree[j].append(i)

    stack = [1]
    parent = [0 for _ in range(N)]  # 각 노드의 부모노드를 저장할 리스트
    visited = [0 for _ in range(N)]  # 방문 여부
    while stack:
        k = stack.pop()
        visited[k-1] = 1  # 방문 처리
        for nxt in tree[k]:  # k와 인접한 노드 탐색
            if visited[nxt-1]:  # 방문 했던 노드라면 continue
                continue
            stack.append(nxt)  # 방문 하지 않았다면 stack에 추가
            visited[nxt-1]  # 방문 처리
            parent[nxt-1] = k  # 부모 노드를 k로 지정
    for i in parent[1:]:  # 결과 출력
        print(i)


solution()