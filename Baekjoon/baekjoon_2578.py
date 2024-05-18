# https://www.acmicpc.net/problem/2578
# 빙고
# Silver IV
def is_bingo(grid, n) -> bool:
    # directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    lines = []
    bingo = 0
    # 행에 대해서 체크
    for i in range(n):
        if sum(grid[i]) == 0:  # i 번째 행이 빙고
            bingo += 1

    # 열에 대해서 체크
    for j in range(n):
        # j 번 열에 대해서
        sum_ = 0
        for i in range(n):
            # i 번째 행
            sum_ += grid[i][j]
        if sum_ == 0:
            bingo += 1

    # 대각선에 대해서 체크
    """
        시작점 : 방향 
        (0,0) : (1,1)
        (n,0) : (-1,1)
    """
    src1 = (0, 0)
    dir1 = (1, 1)
    src2 = (n - 1, 0)
    dir2 = (-1, 1)
    sum_1 = 0
    sum_2 = 0
    for _ in range(5):
        sum_1 += grid[src1[0]][src1[1]]
        sum_2 += grid[src2[0]][src2[1]]
        src1 = (src1[0] + dir1[0], src1[1] + dir1[1])
        src2 = (src2[0] + dir2[0], src2[1] + dir2[1])
    if sum_1 == 0:
        bingo += 1
    if sum_2 == 0:
        bingo += 1

    if bingo >= 3:
        return True
    else:
        return False


def solution():
    N = 5
    grid = []
    nums = []
    pos = dict()
    for i in range(N):
        grid.append(list(map(int, input().split())))
    for j in range(N):
        nums.extend(list(map(int, input().split())))
    idx = 0
    for k in range(N):
        for l in range(N):
            pos[grid[k][l]] = idx
            idx += 1

    for i, n in enumerate(nums):
        if is_bingo(grid, N):
            print(i)
            break
        idx_n = pos[n]
        y, x = divmod(idx_n, N)
        grid[y][x] = 0

    return


solution()
