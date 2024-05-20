# https://www.acmicpc.net/problem/23971
# ZOAC 4
# Bronze III


def solution():
    h, w, n, m = map(int, input().split())

    row = 0
    for _ in range(0,w,m+1):
        row += 1

    col = 0
    for _ in range(0,h,n+1):
        col += 1

    print(row*col)
    
solution()