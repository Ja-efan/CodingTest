# https://www.acmicpc.net/problem/14501
# 퇴사
# Silver III

def solution():
    n = int(input())
    schedule = []  # [t,p]로 구성된 상담 일정 리스트
    for i in range(n):
        schedule.append(list(map(int, input().split())))


