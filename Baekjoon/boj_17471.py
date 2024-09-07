# 게리맨더링
# Gold III
"""
각 구역은 두 개의 선거구 중에 하나로 선택 된다. (1 or 2)
i번째 구역을 j 선거구로 선택하기 전에, 가능한 선택인지 확인한다.
가능한 선택이란,
    1. 한 선거구에 포함된 구역은 모두 연결되어 있어야 한다.
        -> 연결되어 있다: 중간에 통하는 인접한 구역은 0개 이상이어야 한다.
    => 즉, 각 선거구에 속한 구역은 선거구내의 구역들과 모두 연결되어 있어야 한다.
"""

from collections import deque

def is_possible(election_area_1, election_area_2):
    if len(election_area_1) == N or len(election_area_2) == N:
        return False
    # election_area_1
    # area = election_area_1[0]
    if election_area_1:
        visited_1 = set()
        src = list(election_area_1)[0]
        visited_1.add(src)
        dq = deque([src])
        while dq:
            area = dq.popleft()
            for adj_area in adj_list[area]:
                if adj_area in visited_1  or adj_area not in election_area_1:
                    continue
                visited_1.add(adj_area)
                dq.append(adj_area)
        for v in election_area_1:
            if v not in visited_1:
                return False

    if election_area_2:
        # election_area_2
        visited_2 = set()
        src = list(election_area_2)[0]
        visited_2.add(src)
        dq = deque([src])
        while dq:
            area = dq.popleft()
            for adj_area in adj_list[area]:
                if adj_area in visited_2 or adj_area not in election_area_2:
                    continue
                visited_2.add(adj_area)
                dq.append(adj_area)
        for v in election_area_2:
            if v not in visited_2:
                return False

    return True

def dfs(curr_area, election_area_1, election_area_2):
    global diff_population

    #
    if len(visited) == N:
        population_1 = sum([population_list[i] for i in election_area_1])
        population_2 = sum([population_list[i] for i in election_area_2])
        print(population_1, population_2)
        diff_population = min(diff_population, abs(population_2 - population_1))
        return
    visited.add(curr_area)
    # 현재 구역이 1번 선거구에 들어가는 경우
    if is_possible(election_area_1=election_area_1.union({curr_area}), election_area_2=election_area_2):
        for adj_area in adj_list[curr_area]:
            dfs(curr_area=adj_area,
                election_area_1=election_area_1.union({curr_area}),
                election_area_2=election_area_2)
    # 현재 구역이 2번 선거구에 들어가는 경우
    if is_possible(election_area_1=election_area_1, election_area_2=election_area_2.union({curr_area})):
        for adj_area in adj_list[curr_area]:
            dfs(curr_area=adj_area,
                election_area_1=election_area_1,
                election_area_2=election_area_2.union({curr_area}))


def main():
    global adj_list, N
    N = int(input())
    population_list = list(map(int, input().split()))
    for i in range(1, N+1):
        adj_list[i] = list(map(int, input().split()))[1:]

    init_election_area_1 = set()
    init_election_area_2 = set()

    dfs(curr_area=1, election_area_1=init_election_area_1, election_area_2=init_election_area_2)
    print(diff_population)
    return

if __name__ == "__main__":
    N = 0
    population_list = list()
    visited = set()
    adj_list = dict()
    diff_population = 1000
    main()