# https://www.acmicpc.net/problem/2839
# 설탕 배달
# Silver IV

def solution():
    N = int(input())

    cnt5 = 0
    sum_ = 0
    while sum_ < N:  # 5키로 봉지를 최대한 가져간다.
        sum_ += 5
        cnt5 += 1
    if sum_ == N:
        print(cnt5)
        return
    elif (N - sum_) % 3 == 0:  # 나머지를 3으로 채울 수 있다면
        cnt3 = (N-sum_) / 3
        print(int(cnt5 + cnt3))
        return

    while cnt5:
        sum_ -= 5
        cnt5 -= 1
        if ((N-sum_) % 3) == 0:
            cnt3 = int((N-sum_) / 3)
            print(cnt5+cnt3)
            return

    if N % 3 == 0:
        cnt3 = int(N / 3)
        print(cnt3)

    else:


solution()