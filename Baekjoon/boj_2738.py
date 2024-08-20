# 행렬 덧셈
# Bronze III
# https://www.acmicpc.net/problem/2738

def main():
    N, M = map(int, input().split())
    matrix_A = [list(map(int, input().split())) for _ in range(N)]
    matrix_B = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(M):
            matrix_A[r][c] += matrix_B[r][c]
        print(*matrix_A[r])


if __name__ == "__main__":
    main()