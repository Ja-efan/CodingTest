# https://www.acmicpc.net/problem/19637
# IF문 좀 대신 써줘
# Silver III


import sys

input = sys.stdin.readline
output = sys.stdout.write


def solution(): 

    # 사용자 입력
    N, M = map(int, input().split())

    titles = []
    for _ in range(N):
        title, max_ = input().split()
        titles.append((title, int(max_)))

    powers = []
    for _ in range(M):
        powers.append(int(input()))


    # 각 전투력에 맞는 칭호를 찾기 위해 이진탐색 수행
    for power in powers:
        left = 0
        right = N-1
        while left <= right: 
            mid = (left + right) // 2
            if power > titles[mid][1]:
                left = mid + 1
            else :
                right = mid -1
        mid = left
        output(titles[mid][0]+'\n')


solution()


    