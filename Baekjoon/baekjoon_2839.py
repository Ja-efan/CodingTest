# https://www.acmicpc.net/problem/2839
# 설탕 배달
# Silver IV

def solution():
    N = int(input())

    """
    5키로 / 3키로로 N을 채운다. 
    채우지 못하면 -1 
    """
    if N % 5 == 0:
        print(f"{N//5}")
        return

    # divmod 사용
    cnt5, remain = divmod(N, 5)

    while remain % 3 != 0:
        if remain == N:
            print(-1)
            return
        remain += 5
        cnt5 -= 1

    cnt3 = remain // 3

    print(cnt5+cnt3)


solution()