# https://www.acmicpc.net/problem/14501
# 퇴사
# Silver III

def solution():
    n = int(input())
    schedule = []  # [t,p]로 구성된 상담 일정 리스트
    for i in range(n):
        schedule.append(list(map(int, input().split())))
    pop_list = []
    able = []
    check = [0 for _ in range(n)]
    # able : 남은 기간상 가능한 상담만 추린 리스트
    for i in range(n):
        t = schedule[i][0]
        p = schedule[i][1]
        start = i
        end = i + t - 1
        if end > n-1:
            pop_list.append(i)
            continue
        able.append([start, end, p])

    for i in range(len(able)):
        start = able[i][0]
        end = able[i][1]
        pay = able[i][2]
        stack = [i]
        while stack:
            cs = stack.pop()
            start = cs[0]
            end = cs[1]
            p = cs[2]

            for j in range(len(able)):
                if i == j:
                    continue
                next_cs = able[j]
                next_start = next_cs[0]
                next_end = next_cs[1]
                cannot = False
                for k in range(next_start, next_end+1):
                    if k in range(start, end+1):
                        cannot = True
                if cannot:
                    continue

