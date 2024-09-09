# 디저트 카페
"""
12시 방향부터 시계 방향으로 탐색
(1,1) -> (1, -1) -> (-1, -1) -> (-1, 1)

탐색 종료 -> 우측 상단으로 올라가는 방향이면서, 다음 좌표가 시작 좌표

탐색 -> 현재 방향으로 진행하거나, 다음 방향으로 진행하거나

탐색 인자: 현재 좌표, 진행 방향, 먹은 디저트 집합,
"""


# 좌표 유효성 검사 함수
def is_valid(row, col):
    if row < 0 or row >= N or col < 0 or col >= N:
        return False

    return True


def dfs(curr_row, curr_col, curr_direction, dessert_set, start_coord):
    global max_num_dessert

    # 현재 좌표가 시작 지점이면서, 우측 상단으로 올라가는 방향인 경우 -> 디저트 개수 갱신
    if (curr_row, curr_col) == start_coord and curr_direction == 3:
        max_num_dessert = max(max_num_dessert, len(dessert_set))
        return

    # 현재 좌표가 시작 좌표가 아님에도, 현재 좌표의 디저트를 이미 먹은 경우 (같은 종류의 디저트) 반환
    if (curr_row, curr_col) != start_coord and dessert_map[curr_row][curr_col] in dessert_set:
        return

    # 현재 좌표의 디저트를 디저트 집합에 추가
    dessert_set.add(dessert_map[curr_row][curr_col])

    # 현재 방향으로 진행하거나, 방향 전환 하거나
    for i in range(2):
        # 다음 방향 (i=0: 현재 방향 진행, i=1: 방향 전환 후 진행)
        next_direction_i = curr_direction + i
        # 방향이 4 이상이다 -> 의미 없으므로 스킵
        if next_direction_i >= 4:
            continue

        # 이동 방향
        dr, dc = directions[next_direction_i]
        # 다음 좌표
        next_row = curr_row + dr
        next_col = curr_col + dc

        # 다음 좌표가 유효한 경우
        if is_valid(next_row, next_col):
            # 다음 좌표로 DFS 진행
            # 다음 좌표가 형성된 방향으로 진행
            dfs(next_row, next_col, next_direction_i,
                dessert_set=dessert_set,
                start_coord=start_coord)
    # 현재 좌표 디저트 제거 (원복)
    dessert_set.remove(dessert_map[curr_row][curr_col])


# 가능한 좌표들에 대해서 dfs 진행
def dessert_tour():
    # r이 N-2 이상인 경우 시계 방향 회전 후 제자리로 돌아오지 못함
    for r in range(N - 2):
        # c가 0 미만 이거나 N-1 이상인 경우 제자리로 돌아오지 못함
        for c in range(1, N - 1):
            dfs(curr_row=r, curr_col=c, curr_direction=0, dessert_set={dessert_map[r][c]}, start_coord=(r, c))


def main():
    global N, dessert_map, max_num_dessert
    T = int(input())
    for tc in range(1, T + 1):
        max_num_dessert = -1  # testcase 마다 -1 초기화
        # 사용자 입력
        N = int(input())
        dessert_map = [list(map(int, input().split())) for _ in range(N)]
        # 디저트 카페 투어
        dessert_tour()
        # 결과 출력
        print(f"#{tc} {max_num_dessert}")
    return


if __name__ == "__main__":
    import sys
    sys.stdin = open("./testcases/input_2105.txt")

    # global variables
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    max_num_dessert = 0
    N = 0
    dessert_map = list()
    main()